@echo off
REM Build the EasyLink worker into a single .exe (run on Windows).
REM Output: dist\easylink_worker.exe

pyinstaller --onefile --noconsole --collect-all uvicorn --name easylink_worker worker.py

echo.
echo Done. The exe is in dist\easylink_worker.exe
pause