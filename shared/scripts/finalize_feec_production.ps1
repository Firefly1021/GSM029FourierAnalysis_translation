$ErrorActionPreference='Stop'
$libraryRoot=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$bookRoot=[IO.Path]::GetFullPath((Join-Path $libraryRoot 'books/finite-element-exterior-calculus'))
$auditRoot=[IO.Path]::GetFullPath((Join-Path $libraryRoot 'shared/qa/feec-production-20261023'))
$verification=Get-Content -LiteralPath (Join-Path $auditRoot 'verification.json') -Raw | ConvertFrom-Json
$build=Get-Content -LiteralPath (Join-Path $auditRoot 'production-build.json') -Raw | ConvertFrom-Json
if (-not $verification.passed -or -not $build.success) { throw 'Publication requires passed source/build/link checks' }
$source=[IO.Path]::GetFullPath($build.candidate_pdf)
$destination=[IO.Path]::GetFullPath((Join-Path $bookRoot 'output/book-aljabr-zh.pdf'))
if (-not $source.StartsWith($bookRoot+'\.build\',[StringComparison]::OrdinalIgnoreCase)) { throw 'Wrong candidate scope' }
if ($destination -ne ($bookRoot+'\output\book-aljabr-zh.pdf')) { throw 'Wrong publication target' }
if ((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLower() -ne $verification.new_pdf_sha256) { throw 'Audited PDF changed' }
Copy-Item -LiteralPath $source -Destination $destination -Force
if ((Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash.ToLower() -ne $verification.new_pdf_sha256) { throw 'Publication copy mismatch' }
$removed=@()
foreach ($folder in @((Join-Path $bookRoot '.build'),(Join-Path $auditRoot 'prepared'))) {
    $target=[IO.Path]::GetFullPath($folder)
    if ($target -notin @(($bookRoot+'\.build'),($auditRoot+'\prepared'))) { throw 'Unexpected cleanup target' }
    if (-not (Test-Path -LiteralPath $target)) { continue }
    $children=@(Get-ChildItem -LiteralPath $target -Force -Recurse)
    if (@($children | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }).Count) { throw 'Unexpected cleanup link' }
    $files=@($children | Where-Object { -not $_.PSIsContainer })
    $removed+=[pscustomobject]@{path=$target;files=$files.Count;bytes=($files | Measure-Object -Property Length -Sum).Sum}
    Remove-Item -LiteralPath $target -Recurse -Force
}
$readerNoteCache=[IO.Path]::GetFullPath((Join-Path $auditRoot 'intermediate-reader-notes.pdf'))
if ($readerNoteCache -ne ($auditRoot+'\intermediate-reader-notes.pdf')) { throw 'Unexpected reader-note validation cache' }
if (Test-Path -LiteralPath $readerNoteCache) { Remove-Item -LiteralPath $readerNoteCache -Force }
[pscustomobject]@{published_pdf=$destination;sha256=$verification.new_pdf_sha256;pages=$verification.new_pdf_pages;task_created_caches_removed=$removed;remote_push=$false} | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $auditRoot 'publication.json') -Encoding utf8
Write-Output 'Published verified AJbook PDF; book-local build cache and duplicate preparation files removed.'
