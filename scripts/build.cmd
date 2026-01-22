@echo off
setlocal

set DEST=%1

echo Updating gallery list...
python scripts\update_gallery.py
if errorlevel 1 (
  echo Gallery update failed. Fix the issue and try again.
  exit /b 1
)

echo Building site...
if "%DEST%"=="" (
  bundle exec jekyll build
) else (
  bundle exec jekyll build --destination %DEST%
)
