@echo off
chcp 65001

set "project_root=%~dp0"
for %%I in ("%project_root%") do set "parent_path=%%~dpI"
for %%I in ("%parent_path%\..") do set "desired_path=%%~dpI"

set "rcc_path=%desired_path%venv\Lib\site-packages\qt6_applications\Qt\bin\rcc.exe"
set "src_file=%desired_path%res\res.qrc"
set "output_file=%desired_path%src\UI\res_rc.py"

echo %rcc_path%
echo %src_file%

"%rcc_path%" -g python "%src_file%" > "%output_file%"
