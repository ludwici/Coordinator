cd ..
cd ..
source venv/bin/activate

pyinstaller --onefile --noconfirm --noconsole --name "Coordinator" --add-data=res:res main.py --icon=icon.ico --version-file version.rc

deactivate

if [ $? -eq 0 ]; then
  echo "Build completed successfully."
else
  echo "Build failed."
fi

rm Coordinator.spec