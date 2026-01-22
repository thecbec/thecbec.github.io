param(
  [int]$Port = 4001,
  [string]$Host = "127.0.0.1"
)

$ErrorActionPreference = "Stop"

Write-Host "Updating gallery list..." -ForegroundColor Cyan
python scripts/update_gallery.py
if ($LASTEXITCODE -ne 0) {
  Write-Host "Gallery update failed. Fix the issue and try again." -ForegroundColor Red
  exit $LASTEXITCODE
}

Write-Host "Starting Jekyll server on $Host`:$Port..." -ForegroundColor Cyan
bundle exec jekyll serve --host $Host --port $Port
