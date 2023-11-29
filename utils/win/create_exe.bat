@echo off
chcp 65001

cd ..
cd ..
call venv\Scripts\activate

pyinstaller --onefile --noconfirm --noconsole --name "Coordinator" --add-data "res;res" main.py --icon=icon.ico --version-file version.rc

call venv\Scripts\deactivate

if %errorlevel% == 0 (
    echo Build completed successfully.
) else (
    echo Build failed.
)

del "Coordinator.spec"