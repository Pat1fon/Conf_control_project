@echo off
chcp 65001 > nul
echo Параметры vfs, script
.venv\Scripts\python.exe src\practice_1_CLI.py --vfs ./vfs_config.json --script start_script.txt
pause