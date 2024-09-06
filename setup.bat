@echo off

REM Clone the existing arcgispro-py3 environment to genai-py3
call conda create --name genai-auto-py3 --clone arcgispro-py3

call proswap genai-auto-py3

REM  Change back to the original directory
cd /d "%ORIGINAL_DIR%"

:: Print the current directory to verify
echo Back in directory: %CD%

REM Install dependencies from requirements.txt
call pip install -r requirements.txt

endlocal