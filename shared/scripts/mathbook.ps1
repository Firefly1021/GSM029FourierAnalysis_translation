param([Parameter(ValueFromRemainingArguments=$true)][string[]]$BookArguments)
$ErrorActionPreference = 'Stop'
$systemRoot = Split-Path -Parent $PSScriptRoot
$runtimeFile = Join-Path $systemRoot 'config/runtime.local.json'
$pythonExecutable = $null
if (Test-Path -LiteralPath $runtimeFile) {
    $runtime = Get-Content -LiteralPath $runtimeFile -Raw | ConvertFrom-Json
    if (Test-Path -LiteralPath $runtime.python) { $pythonExecutable = $runtime.python }
}
if (-not $pythonExecutable) {
    $uvCommand = Get-Command uv -ErrorAction SilentlyContinue
    if ($uvCommand) { $candidate = & $uvCommand.Source python find; if ($LASTEXITCODE -eq 0) { $pythonExecutable = $candidate.Trim() } }
}
if (-not $pythonExecutable) {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if ($pythonCommand -and $pythonCommand.Source -notlike '*WindowsApps*') { $pythonExecutable = $pythonCommand.Source }
}
if (-not $pythonExecutable) { throw 'No usable Python runtime found. Configure shared/config/runtime.local.json or install Python.' }
& $pythonExecutable -X utf8 (Join-Path $PSScriptRoot 'library_cli.py') @BookArguments
exit $LASTEXITCODE
