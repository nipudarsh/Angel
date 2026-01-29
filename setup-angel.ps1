<#[
.SYNOPSIS
    Setup script for ANGEL.
.DESCRIPTION
    Creates project structure, installs dependencies, and initializes git.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$ProjectPath,

    [Parameter(Mandatory=$true)]
    [string]$RepoUrl,

    [Parameter(Mandatory=$false)]
    [string]$StoragePath,

    [Parameter(Mandatory=$false)]
    [string]$AdminUsername,

    [Parameter(Mandatory=$false)]
    [string]$AdminPassword,

    [switch]$SkipGitHub,
    [switch]$SkipTests,
    [switch]$DevMode,
    [switch]$VerboseOutput
)

$ErrorActionPreference = "Stop"
$logFile = Join-Path $ProjectPath "setup.log"

function Write-Log {
    param([string]$Message)
    $timestamp = Get-Date -Format "u"
    $line = "$timestamp $Message"
    $line | Tee-Object -FilePath $logFile -Append
}

function Ensure-Tool {
    param([string]$Name, [string]$Command)
    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
        throw "$Name is required but not found in PATH."
    }
}

try {
    Write-Log "Starting ANGEL setup."
    Ensure-Tool -Name "Python" -Command "python"
    Ensure-Tool -Name "Git" -Command "git"

    if (-not (Test-Path $ProjectPath)) {
        New-Item -ItemType Directory -Path $ProjectPath | Out-Null
    }

    Push-Location $ProjectPath

    if (-not (Test-Path ".git")) {
        git init | Out-Null
    }

    if (-not (Test-Path ".venv")) {
        python -m venv .venv
    }

    $venvPython = Join-Path $ProjectPath ".venv\Scripts\python.exe"
    if (-not (Test-Path $venvPython)) {
        throw "Virtual environment not created."
    }

    & $venvPython -m pip install --upgrade pip setuptools wheel
    & $venvPython -m pip install --prefer-binary -r requirements.txt
    if ($DevMode) {
        & $venvPython -m pip install --prefer-binary -r requirements-dev.txt
    }
    & $venvPython -m pip install -e .

    if (-not $SkipGitHub) {
        git remote add origin $RepoUrl 2>$null
    }

    if (-not $SkipTests) {
        & $venvPython -m pytest
    }

    Write-Log "Setup complete."
} catch {
    Write-Log "Error: $($_.Exception.Message)"
    throw
} finally {
    Pop-Location
}
