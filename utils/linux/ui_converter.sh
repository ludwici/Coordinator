#!/bin/bash

#/PycharmProjects/Coordinator/ui$ ../utils/linux/ui_converter.sh MainWindow.ui MainWindow.py

project_root="$(dirname "$0")"
parent_path="$(dirname "$project_root")"
desired_path="$(cd "$parent_path"/.. && pwd)"
output_path="$desired_path/src/UI/$2"

uic_path="$desired_path/venv/bin/pyside6-uic"

"$uic_path" "$1" -o "$output_path"
python "$desired_path/utils/py/import_fix.py" "$output_path"