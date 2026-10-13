param([switch]$VerifyOnly)
$ErrorActionPreference = 'Stop'
$ArgsList = @()
if ($VerifyOnly) { $ArgsList += '--verify-only' }
py (Join-Path $PSScriptRoot 'install.py') @ArgsList
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
