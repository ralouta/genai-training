@echo off
setlocal

REM Install dependencies from requirements.txt
echo Installing dependencies from requirements.txt...
call pip install -r requirements.txt || (
    echo Failed to install dependencies
    exit /b 1
)

endlocal