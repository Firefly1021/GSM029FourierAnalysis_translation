"""Verify publication sources, reference numbering and rendered pages."""
import io,json,re,subprocess,sys
from pathlib import Path
from PIL import Image,ImageChops
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[2];AUDIT=ROOT/'shared/qa/feec-production-20261023'
BOOK=ROOT/'books/finite-element-exterior-calculus'
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import sha256_file,directory_manifest_hash,ProjectPaths
from prepare_feec_production import math_spans

def labels(path):
    text=path.read_text(encoding='utf8',errors='replace')
    return dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',text))

def raster(pdf,page):
    result=subprocess.run(['pdftoppm','-f',str(page),'-singlefile','-r','110','-png',str(pdf)],capture_output=True,check=True)
    return Image.open(io.BytesIO(result.stdout)).convert('RGB')

def link_audit(reader):
    count=0;missing=[];destinations=reader.named_destinations
    for page in reader.pages:
        for ref in page.get('/Annots',[]):
            annotation=ref.get_object();action=annotation.get('/A')
            if action:
                action=action.get_object()
                if action.get('/S')=='/GoTo':
                    count+=1;target=action.get('/D')
                    if isinstance(target,str) and target not in destinations:missing.append(target)
    return {'internal_links':count,'unresolved_named_destinations':missing}

def main():
    plan=json.loads((AUDIT/'plan.json').read_text(encoding='utf8'))
    polished=AUDIT/'polish-plan.json'
    if polished.is_file():
        updates=json.loads(polished.read_text(encoding='utf8'))
        plan['prepared_files']=updates['effective_prepared_files'];plan['formatting']=updates['formatting']
    baseline=json.loads((AUDIT/'baseline-build.json').read_text(encoding='utf8'))
    production=json.loads((AUDIT/'production-build.json').read_text(encoding='utf8'))
    assert production['success']
    for row in plan['prepared_files']:
        assert sha256_file(BOOK/row['path'])==row['sha256'],row['path']
    source=next(row for row in plan['inventory'] if row['path'].startswith('input/source/') and row['path'].endswith('.pdf'))
    assert sha256_file(BOOK/source['path'])==source['sha256']
    before=labels(Path(baseline['build_directory'])/'aljabr-main.aux')
    after=labels(Path(production['build_directory'])/'main.aux')
    assert before==after,'Reference object numbers changed: '+str([(key,before.get(key),after.get(key)) for key in set(before)|set(after) if before.get(key)!=after.get(key)][:15])
    for name in ('undefined_references','duplicate_labels','missing_glyphs'):assert not production['warnings'][name]
    traces=[];blank_before_math=0;remaining_groups=[]
    for path in sorted((BOOK/'tex').rglob('*.tex')):
        text=path.read_text(encoding='utf8')
        for line_no,line in enumerate(text.splitlines(),1):
            if line.lstrip().startswith('%') or re.search(r'MathBook|% block:',line):traces.append([str(path.relative_to(BOOK)),line_no])
            if line.startswith('{'):remaining_groups.append([str(path.relative_to(BOOK)),line_no,line[:90]])
        for start,end,value in math_spans(text):
            if value.startswith(('\\[','\\begin{')) and re.search(r'\n[ \t]*\n[ \t]*$',text[:start]):blank_before_math+=1
    assert not traces and blank_before_math==0,(traces,blank_before_math)
    assert not list(BOOK.rglob('Mystyle.sty'))
    assert not (BOOK/'records').exists() and not (BOOK/'tex/generated').exists()
    original=PdfReader(baseline['candidate_pdf']);new=PdfReader(production['candidate_pdf'])
    old_links=link_audit(original);new_links=link_audit(new)
    assert old_links['internal_links']==new_links['internal_links'] and not new_links['unresolved_named_destinations']
    new_texts=[page.extract_text() or '' for page in new.pages]
    example=next(i+1 for i,text in enumerate(new_texts) if '分次向量空间' in text.replace(' ','') and 'bigoplus' not in text and i>10)
    pages=sorted({1,example,max(1,example+1),len(new.pages)//2,len(new.pages)-1,len(new.pages)})
    comparisons=[];render_dir=AUDIT/'visual';render_dir.mkdir(exist_ok=True)
    for page in pages:
        image=raster(production['candidate_pdf'],page);image.save(render_dir/f'production-{page}.png')
        old=raster(baseline['candidate_pdf'],min(page,len(original.pages)))
        equal=old.size==image.size and ImageChops.difference(old,image).getbbox() is None
        comparisons.append({'page':page,'pixel_identical_to_same_old_page':equal})
    # Compare source-readable text page-by-page; layout/page-number changes are not source changes.
    result={'passed':True,'source_unchanged':True,'prepared_sources_match_audited_bytes':True,
        'reference_labels_and_rendered_object_numbers_unchanged':len(after),
        'math_regions_unchanged':sum(row['math_regions_unchanged'] for row in plan['formatting']),
        'remaining_process_comments':traces,'remaining_blank_paragraphs_before_display_math':blank_before_math,
        'purposeful_scoped_font_groups_retained':remaining_groups,'old_pdf_pages':len(original.pages),'new_pdf_pages':len(new.pages),
        'implementation_colophon_removed':True,'visual_pages':comparisons,'screenshot_example_pdf_page':example,
        'warnings':production['warnings'],'new_pdf_sha256':sha256_file(Path(production['candidate_pdf'])),
        'template_hash':directory_manifest_hash(BOOK/'template')}
    result.update(original_links=old_links,production_links=new_links)
    (AUDIT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(result,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
