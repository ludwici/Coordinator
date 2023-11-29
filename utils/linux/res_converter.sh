#!/bin/bash

project_root="$(dirname "$0")"
parent_path="$(dirname "$project_root")"
desired_path="$(cd "$parent_path"/.. && pwd)"

rcc_path="$desired_path/venv/bin/pyside6-rcc"
src_file="$desired_path/res/res.qrc"
output_file="$desired_path/src/UI/res_rc.py"

echo "$rcc_path"
echo "$src_file"

"$rcc_path" "$src_file" > "$output_file"
