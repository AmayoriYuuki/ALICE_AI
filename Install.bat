@echo off
title ALICE v1.6.5 Installer
color 0A
echo [*] Fancy Installer for ALICE v1.6.5
echo ---------------------------------------
echo.
echo Checking Python environment...

python --version
IF %ERRORLEVEL% NEQ 0 (
    echo [!] Python not found. Please install Python 3.9.7
    pause
    exit /b
)

echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo [✔] Installation complete!
pause
