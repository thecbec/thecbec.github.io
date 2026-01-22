@echo off
setlocal

set PORT=%1
if "%PORT%"=="" set PORT=4001

set HOST=%2
if "%HOST%"=="" set HOST=127.0.0.1

echo Updating gallery list...
python scripts\update_gallery.py
if errorlevel 1 (
  echo Gallery update failed. Fix the issue and try again.
  exit /b 1
)

echo Starting Jekyll server on %HOST%:%PORT%...
bundle exec jekyll serve --host %HOST% --port %PORT%
