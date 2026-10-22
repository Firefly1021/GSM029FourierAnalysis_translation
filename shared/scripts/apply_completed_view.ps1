param([Parameter(Mandatory=$true)][string]$Plan)
$ErrorActionPreference='Stop'
$libraryRoot=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$planPath=(Resolve-Path -LiteralPath $Plan).Path
$planData=Get-Content -LiteralPath $planPath -Raw | ConvertFrom-Json
if ($planData.library_root -ne $libraryRoot) { throw 'Incorrect library root' }
if ((git -C $libraryRoot branch --show-current).Trim() -ne 'main') { throw 'Completed-book migration requires the registered main checkout' }
function Resolve-BookTarget([string]$bookRoot,[string]$relative) {
    $target=[IO.Path]::GetFullPath((Join-Path $bookRoot $relative))
    if (-not $target.StartsWith($bookRoot+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)) { throw "Target escapes selected book: $target" }
    return $target
}
# Verify every planned byte and every move target before changing any book.
foreach ($book in $planData.books) {
    if ($book.book_id -notmatch '^[a-z0-9]+(-[a-z0-9]+)*$') { throw 'Invalid explicit book-id' }
    $bookRoot=[IO.Path]::GetFullPath((Join-Path $libraryRoot ('books/'+$book.book_id)))
    if (Test-Path -LiteralPath (Join-Path $bookRoot 'records')) { throw 'Records already exist; refuse a second migration' }
    foreach ($file in $book.inventory) {
        $target=Resolve-BookTarget $bookRoot $file.from
        $info=Get-Item -LiteralPath $target -Force
        if ($info.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Unexpected link' }
        if ($info.Length -ne $file.bytes -or (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLower() -ne $file.sha256) { throw "Original bytes changed: $target" }
    }
    foreach ($move in $book.moves) {
        $source=Resolve-BookTarget $bookRoot $move.from
        $destination=Resolve-BookTarget $bookRoot $move.to
        if ($move.from -notin @('config','formulae','glossary','qa','structured','translation','archive','PLANS.md','PROJECT_STATUS.md','TYPESETTING.md','workspace/crops')) { throw 'Unapproved move' }
        if ($move.to -notlike 'records/*' -or (Test-Path -LiteralPath $destination)) { throw 'Unsafe destination' }
    }
}
$receipts=@()
foreach ($book in $planData.books) {
    $bookRoot=[IO.Path]::GetFullPath((Join-Path $libraryRoot ('books/'+$book.book_id)))
    New-Item -ItemType Directory -Path (Join-Path $bookRoot 'records') | Out-Null
    foreach ($move in $book.moves) {
        $source=Resolve-BookTarget $bookRoot $move.from
        $destination=Resolve-BookTarget $bookRoot $move.to
        Move-Item -LiteralPath $source -Destination $destination
    }
    foreach ($file in $book.inventory) {
        $target=Resolve-BookTarget $bookRoot $file.to
        if ((Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLower() -ne $file.sha256) { throw "Moved content changed: $target" }
    }
    $deleted=0;[long]$deletedBytes=0
    foreach ($removal in $book.removals) {
        $target=Resolve-BookTarget $bookRoot $removal.path
        if ($removal.path -match '^(input|tex|template(?:-accepted)?|output)(/|$)') { throw 'Formal project input/output is protected' }
        $item=Get-Item -LiteralPath $target -Force
        $files=if ($item.PSIsContainer) { @(Get-ChildItem -LiteralPath $target -File -Recurse -Force) } else { @($item) }
        [long]$bytes=($files | Measure-Object -Property Length -Sum).Sum
        if ($files.Count -ne $removal.files -or $bytes -ne $removal.bytes) { throw "Deletion inventory changed: $target" }
        if ($item.PSIsContainer) { Remove-Item -LiteralPath $target -Recurse -Force } else { Remove-Item -LiteralPath $target -Force }
        $deleted+=$files.Count;$deletedBytes+=$bytes
    }
    $receipts+=[pscustomobject]@{ book_id=$book.book_id; moves=$book.moves.Count; deleted_files=$deleted; deleted_bytes=$deletedBytes; root_after=@(Get-ChildItem -LiteralPath $bookRoot -Force | Select-Object -ExpandProperty Name) }
    Write-Output ("Completed edition organized: "+$book.book_id)
}
[pscustomobject]@{ plan_sha256=(Get-FileHash -LiteralPath $planPath -Algorithm SHA256).Hash.ToLower(); books=$receipts; remote_push=$false } | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath ([IO.Path]::ChangeExtension($planPath,'.receipt.json')) -Encoding utf8
