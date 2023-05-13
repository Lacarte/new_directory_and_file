@echo off
set current_dir=%cd%
for /f "delims=" %%a in ('where f') do set "executablePath=%%~dpa"
echo %current_dir%
python  %executablePath%random-df.py -root_dir %current_dir% -ford f
pause