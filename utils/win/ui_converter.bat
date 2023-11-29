@echo off
chcp 65001
setlocal
@REM /PycharmProjects/Coordinator/ui$ ../utils/win/ui_converter.bat MainWindow.ui MainWindow.py

set "project_root=%~dp0"
for %%I in ("%project_root%") do set "parent_path=%%~dpI"
for %%I in ("%parent_path%\..") do set "desired_path=%%~dpI"
set "output_path=%desired_path%src\UI\%2"

set "uic_path=%desired_path%venv\Lib\site-packages\qt6_applications\Qt\bin\uic.exe"

"%uic_path%" -g python %1 -o "%output_path%"
python "%desired_path%utils\py\import_fix.py" "%output_path%"
endlocal