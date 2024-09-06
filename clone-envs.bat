@echo off

REM Clone the existing arcgispro-py3 environment to genai-py3
echo Cloning arcgispro-py3 to genai-auto-py3...
call conda create --name genai-auto-py3 --clone arcgispro-py3 || (
    echo Failed to clone arcgispro-py3
    exit /b 1
)

REM Swap to the new environment
echo Swapping to genai-auto-py3...
call proswap genai-auto-py3 || (
    echo Failed to swap to genai-auto-py3
    exit /b 1
)

