param(
  [string]$Destination = ""
)

$ErrorActionPreference = "Stop"

Write-Host "Updating gallery list..." -ForegroundColor Cyan
python scripts/update_gallery.py
if ($LASTEXITCODE -ne 0) {
  Write-Host "Gallery update failed. Fix the issue and try again." -ForegroundColor Red
  exit $LASTEXITCODE
}

Write-Host "Building site..." -ForegroundColor Cyan
if ($Destination -ne "") {
  bundle exec jekyll build --destination $Destination
} else {
  bundle exec jekyll build
}
