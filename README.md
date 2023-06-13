# Tykhe Grid Generator
Simple app to generate grids using pillow library and python.

## Installation

No installation is required. Simply download the executable from [Releases](https://github.com/flash-fan/Grid_Generator/releases) and run it.

## Compiling

This project was built using [PyInstaller](https://github.com/pyinstaller/pyinstaller). To build it yourself, follow these steps:

1. Generate a spec file with the given command
```bash
pyinstaller --name {AppName} --onefile ./main.py --add-data="border.png;."
```
2. Use Generated spec file to build an executable
```bash
pyinstaller ./{AppName}.spec
```

It will generate an executable in the `/dist` folder

## Usage

- Run the .exe file
- Select the folder in which cards are stored (each card must be of dimensions 600x800px)
- Specify the number of columns to be in the grid
- Grid will be generated automatically in the same folder as the exe file with the name `grid.png` (or a custom name, if one is provided)


## Features to be added
- Support for background images
- ~~Colour layer behind the grid~~ [2023-04-30]
- ~~Horizontal grid option~~ [2023-04-29]
- ~~Custom names for grid~~ [2023-04-29]
- Custom location to save the grid
- Grid formation for uneven number of images
- Option to split a grid into two or more images
- Allow for alphabetical v/s custom sorting
