$ErrorActionPreference='Stop'
$libraryRoot=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$bookRoot=[IO.Path]::GetFullPath((Join-Path $libraryRoot 'books/finite-element-exterior-calculus'))
$auditRoot=[IO.Path]::GetFullPath((Join-Path $libraryRoot 'shared/qa/feec-production-20261023'))
$recordRoot=[IO.Path]::GetFullPath((Join-Path $libraryRoot 'shared/book-records/finite-element-exterior-calculus'))
$plan=Get-Content -LiteralPath (Join-Path $auditRoot 'plan.json') -Raw | ConvertFrom-Json
if ($plan.book_root -ne $bookRoot -or -not $plan.discard_user_modified_legacy_chapter) { throw 'Wrong explicitly authorized target' }
if (Test-Path -LiteralPath $recordRoot) { throw 'External records already exist' }
foreach ($row in $plan.inventory) {
    $target=[IO.Path]::GetFullPath((Join-Path $bookRoot $row.path))
    if (-not $target.StartsWith($bookRoot+'\',[StringComparison]::OrdinalIgnoreCase)) { throw 'Inventory escaped selected book' }
    if ((Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLower() -ne $row.sha256) { throw "Changed since audit: $target" }
}
foreach ($row in $plan.prepared_files) {
    $target=Join-Path (Join-Path $auditRoot 'prepared') $row.path
    if ((Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLower() -ne $row.sha256) { throw 'Prepared bytes changed' }
}
foreach ($relative in @('tex','template')) {
    $target=[IO.Path]::GetFullPath((Join-Path $bookRoot $relative))
    if ($target -notin @(($bookRoot+'\tex'),($bookRoot+'\template'))) { throw 'Unexpected recursive replacement target' }
    if (@(Get-ChildItem -LiteralPath $target -Recurse -Force | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }).Count) { throw 'Unexpected reparse point' }
}
New-Item -ItemType Directory -Path (Split-Path -Parent $recordRoot) -Force | Out-Null
Move-Item -LiteralPath (Join-Path $bookRoot 'records') -Destination $recordRoot
foreach ($relative in @('tex','template')) {
    $target=[IO.Path]::GetFullPath((Join-Path $bookRoot $relative))
    Remove-Item -LiteralPath $target -Recurse -Force
    Copy-Item -LiteralPath (Join-Path (Join-Path $auditRoot 'prepared') $relative) -Destination $target -Recurse
}
$legacyOutput=[IO.Path]::GetFullPath((Join-Path $bookRoot 'output/book-zh.pdf'))
if ($legacyOutput -ne $bookRoot+'\output\book-zh.pdf') { throw 'Unexpected old-edition output target' }
if (Test-Path -LiteralPath $legacyOutput) { Remove-Item -LiteralPath $legacyOutput -Force }
$outputMarker=Join-Path $bookRoot 'output/.gitkeep'
if (Test-Path -LiteralPath $outputMarker) { Remove-Item -LiteralPath $outputMarker -Force }
foreach ($row in $plan.prepared_files) {
    if ((Get-FileHash -LiteralPath (Join-Path $bookRoot $row.path) -Algorithm SHA256).Hash.ToLower() -ne $row.sha256) { throw 'Production source mismatch' }
}
[pscustomobject]@{book_id=$plan.book_id; old_tex_and_template_replaced=$true; legacy_pdf_deleted=$true; user_dirty_legacy_edit_discarded_as_requested=$true; records_moved_to=$recordRoot; plan_sha256=(Get-FileHash -LiteralPath (Join-Path $auditRoot 'plan.json') -Algorithm SHA256).Hash.ToLower()} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $auditRoot 'execution.json') -Encoding utf8
Write-Output 'FEEC now contains one AJbook source edition; process records are outside books/.'
