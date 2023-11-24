@echo off
set "current_dir=%cd%"
if "%current_dir:~-1%"=="\" set "current_dir=%current_dir%\"

for /f "delims=" %%a in ('where d') do set "executablePath=%%~dpa"
echo current path : %current_dir%
python "%executablePath%main.py" -root_dir "%current_dir%" -file_or_directory d

