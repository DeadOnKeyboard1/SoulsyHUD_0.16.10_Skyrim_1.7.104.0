<#
.SYNOPSIS
    Packages ONLY the SoulsyHUD Skyrim 1.7.104.0 compatibility patch archive.
.DESCRIPTION
    Creates a Vortex/MO2-ready ZIP containing SoulsyHUD.dll, SoulsyHUD.pdb,
    the fixed MCM config.json, and all third-party license files.
#>
[CmdletBinding()]
param(
    [string]$BuildDir = "",
    [string]$OutputDir = "releases",
    [string]$ArchiveName = "SoulsyHUD_0.16.10_Skyrim_1.7.104.0.zip"
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

$pythonArgs = @(
    (Join-Path $ScriptDir "package_patch.py"),
    "--output-dir", $OutputDir,
    "--archive-name", $ArchiveName
)

if ($BuildDir) {
    $pythonArgs += @("--build-dir", $BuildDir)
}

python @pythonArgs
if ($LASTEXITCODE -ne 0) {
    Write-Error "Packaging script failed with exit code $LASTEXITCODE"
}
