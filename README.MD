### What this?
Coordinator it's a simple tool for displaying normalized texture coordinates. It will be used in <TexCoord> xml-tag in you addons
### How to usage
Just run `Coordinator.exe` and select any image  
Supported formats: `png`, `jpg`, `tga`, `blp`  
Also you can run Coordinator from cmd:
`Coordinator.exe path_to_image` and then tool open you image  
![](https://i.imgur.com/1sLA4or.gif)

You can put your coords in `TexCoords` field and press `Apply` button, to shown selected rectangle

### Does this simple tool size more than 40 megabytes?
Because exe file contains everything needed to run pyQt project
### How to build
You can use some my scripts for this.
1. Choose you platform. If you used linux, run `utils/linux/setup.sh` first  
1.1. If you modified `*.ui` file, use `ui_converter` script for converting to python-file  
1.2. If modified resources file (`res/res.qrc`), run `res_converter`  
2. Run `main.py` to start program
3. Run `create_exe.bat` to make executable file