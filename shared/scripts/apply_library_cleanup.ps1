param([Parameter(Mandatory=$true)][string]$Plan)
$ErrorActionPreference = 'Stop'
$libraryRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$planPath = (Resolve-Path -LiteralPath $Plan).Path
$planData = Get-Content -LiteralPath $planPath -Raw | ConvertFrom-Json
if ($planData.library_root -ne $libraryRoot -or $planData.authorization -ne 'user-request-20261022-remove-completed-book-intermediates') { throw 'Wrong cleanup context' }
$validatedTargets = @()
foreach ($item in $planData.targets) {
    $targetPath = [IO.Path]::GetFullPath((Join-Path $libraryRoot $item.path))
    if (-not $targetPath.StartsWith($libraryRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw "Out of library: $targetPath" }
    if ($item.path -match '^books/[^/]+/(template(?:-accepted)?|input)(/|$)' -or $item.path -in @('books','shared','.git')) { throw "Protected target: $targetPath" }
    if (-not ($planData.allowed_prefixes | Where-Object { $item.path.StartsWith($_, [StringComparison]::Ordinal) })) { throw "Unapproved prefix: $targetPath" }
    $targetItem = Get-Item -LiteralPath $targetPath -Force
    if ($targetItem.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Link target: $targetPath" }
    $targetFiles = if ($targetItem.PSIsContainer) { @(Get-ChildItem -LiteralPath $targetPath -File -Recurse -Force) } else { @($targetItem) }
    if ($targetItem.PSIsContainer -and @(Get-ChildItem -LiteralPath $targetPath -Directory -Recurse -Force | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }).Count) { throw "Linked directory: $targetPath" }
    $targetBytes = ($targetFiles | Measure-Object -Property Length -Sum).Sum
    if ($targetFiles.Count -ne $item.files -or [long]$targetBytes -ne [long]$item.bytes) { throw "Inventory changed: $targetPath" }
    $validatedTargets += [pscustomobject]@{ path=$targetPath; relative=$item.path; files=$targetFiles.Count; bytes=[long]$targetBytes; directory=$targetItem.PSIsContainer }
}
$results = @()
foreach ($target in $validatedTargets) {
    if ($target.directory) { Remove-Item -LiteralPath $target.path -Recurse -Force } else { Remove-Item -LiteralPath $target.path -Force }
    if (Test-Path -LiteralPath $target.path) { throw "Not removed: $($target.path)" }
    $results += [pscustomobject]@{ path=$target.relative; files=$target.files; bytes=$target.bytes; removed=$true }
}
$receiptPath = [IO.Path]::ChangeExtension($planPath, '.receipt.json')
[pscustomobject]@{ plan=$planPath; plan_sha256=(Get-FileHash -LiteralPath $planPath -Algorithm SHA256).Hash.ToLower(); completed=(Get-Date).ToString('o'); removed=$results; files=($results | Measure-Object -Property files -Sum).Sum; bytes=($results | Measure-Object -Property bytes -Sum).Sum } | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $receiptPath -Encoding utf8
Write-Output "Removed $($results.Count) audited targets; receipt: $receiptPath"
