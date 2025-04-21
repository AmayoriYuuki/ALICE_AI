@echo off
title ALICE v1.6.5 Uninstaller
color 0C
echo [!] Uninstalling ALICE...

rmdir /s /q venv
del /q alice.py
del /q requirements.txt
del /q Install.bat
del /q Uninstall.bat
del /q README.txt

echo [✔] ALICE Uninstalled.
pause
