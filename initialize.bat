@echo off


REM Save the current directory (the directory where the batch file was run from)
set "ORIGINAL_DIR=%CD%"
echo Original directory: "%ORIGINAL_DIR%"

REM Get the current user's profile directory
set USERPROFILE=%USERPROFILE%


setlocal enabledelayedexpansion

REM Ensure arcgispro_path is set
set "arcgispro_path=C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3"

REM Print the original path
echo The path of arcgispro-py3 is: %arcgispro_path%

REM Replace 'envs\arcgispro-py3' with 'Scripts\proenv.bat'
set "arcgispromodified_path=!arcgispro_path:envs\arcgispro-py3=Scripts\proenv.bat!"

REM Print the modified path
echo The modified path is: !arcgispromodified_path!

REM Check if the modified path is correct
if not exist "!arcgispromodified_path!" (
    echo The modified path does not exist: !arcgispromodified_path!
    exit /b 1
)

REM Activate the arcgispro-py3 environment
call "!arcgispromodified_path!" conda create --name genai-auto-py3 --clone arcgispro-py3

endlocal