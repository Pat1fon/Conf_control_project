@echo off
chcp 65001 > nul
.venv\Scripts\python.exe src\practice_1_CLI.py --vfs ./vfs_config.json
pause
