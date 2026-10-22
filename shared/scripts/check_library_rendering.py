"""Read-only raster spot comparisons of clean candidates and accepted PDFs."""
import io,json,subprocess,os,sys
from pathlib import Path
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[2];REPORT=Path(os.environ.get('MATHBOOK_INTEGRATION_REPORT',str(ROOT/'shared/qa/integration-20261022')))
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths

def raster(path,page):
    result=subprocess.run(['pdftoppm','-f',str(page),'-singlefile','-r','72','-png',str(path)],capture_output=True,check=True)
    return Image.open(io.BytesIO(result.stdout)).convert('RGB')

def main():
    builds=json.loads((REPORT/'builds.json').read_text(encoding='utf8'))
    assert builds['passed'] and len(builds['results'])==7
    results=[]
    for row in builds['results']:
        selected=ProjectPaths(ROOT).book(row['book_id']);book=selected.root;binding=json.loads(selected.binding_file.read_text(encoding='utf8'))
        original=book/binding['final_output'];candidate=Path(row['candidate_pdf'])
        pages=sorted({1,max(1,row['candidate_pdf_pages']//2),row['candidate_pdf_pages']})
        samples=[]
        for page in pages:
            a=raster(original,page);b=raster(candidate,page)
            identical=a.size==b.size and ImageChops.difference(a,b).getbbox() is None
            item={'page':page,'same_dimensions':a.size==b.size,'pixel_identical_at_72dpi':identical}
            if not identical:
                directory=REPORT/'render-differences'/row['book_id'];directory.mkdir(parents=True,exist_ok=True)
                a.save(directory/f'p{page}-original.png');b.save(directory/f'p{page}-candidate.png')
                item['review_images']=str(directory)
            samples.append(item)
        results.append({'book_id':row['book_id'],'samples':samples})
        print(row['book_id'],samples,flush=True)
    (REPORT/'rendering-spot-comparison.json').write_text(json.dumps({'scope':'First/middle/last page raster comparison, not mathematical acceptance.','results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf8')

if __name__=='__main__':main()
