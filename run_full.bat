@echo off
chcp 65001 > nul
echo Параметры vfs, script
.venv\Scripts\python.exe src\practice_1_CLI.py --vfs ./my_virtual_vfs --script start_script.txt
pause