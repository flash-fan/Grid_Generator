# Grid_Generator
Simple app to generate grids using pillow library and python.

## Installation: 

No installation is required. Simply download the executable from [Releases](https://github.com/flash-fan/Grid_Generator/releases) and run it.

## Compiling: 

This project was built using [PyInstaller](https://github.com/pyinstaller/pyinstaller). To build it yourself, follow these steps:

1. Generate a spec file with the given command
```bash
pyinstaller --name GridGenerator --onefile ./main.py
```
2. Use Generated spec file to build an executable
```bash
pyinstaller .\GridGenerator.spec
```

It will generate an executable in the `/dist` folder

## Requirements: 
- Active Internet connection (required to fetch a border from imgur)

## Usage: 

- Run the .exe file
- Select the folder in which cards are stored (each card must be of dimensions 600x800px)
- Specify the number of columns to be in the grid
- Grid will be generated automatically in the same folder as the exe file with the name `grid.png`


## Features to be added:
- Support for background images
- Colour layer behind the grid 
- Horizontal grid option
- Custom names for grid 
- Custom location to save the grid
