@echo off
setlocal enabledelayedexpansion

REM Set the working directory to the directory of the batch file
cd /d "%~dp0"

REM Check if a folder is dragged and dropped
if "%~1"=="" (
    echo Please drag and drop a folder onto this script.
    pause
    exit /b
)

REM Get the full path of the dragged folder
set "folderPath=%~1"

call conda activate base

python main.py "!folderPath!"

pause