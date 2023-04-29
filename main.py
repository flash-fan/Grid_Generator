import re
import sys
from PIL import Image
import tkinter as tk
from tkinter import filedialog, simpledialog
import os
import questionary as qr

# Constants
IMG_HEIGHT = 800
IMG_WIDTH = 600
BORDER_URL = "https://i.imgur.com/AMBdG9m.png"
PADDING = 121
BRDR_HEIGHT = 155


class Grid:
    def __init__(self) -> None:
        self.imgs = []
        self.root = tk.Tk()
        self.root.withdraw()
        self.borderName = self.resource_path("border.png")
        # self.imgFetch()

        # Asking the user for which types of grid they want to generate

        gridTypes = ["Horizontal", "Slanted", "Both"]
        gridType = qr.select(
            "Choose which type of grid you want to generate:",
            choices=gridTypes,
            default=gridTypes[0],
        ).ask()

        # Asking the user for the directory in which cards are stored
        # + the number of columns in the grid
        self.dirChoose()
        self.columnChoose()

        if gridType == gridTypes[0]:
            self.horizontalGrid()
        elif gridType == gridTypes[1]:
            self.verticalGrid()
        else:
            self.horizontalGrid()
            self.verticalGrid()

    def isValid(self, filename):
        # Check if the filename contains any invalid characters
        if re.search(r'[\\/:*?"<>|]', filename):
            return False

        # Check if the filename starts with a reserved name
        reserved_names = [
            "CON",
            "PRN",
            "AUX",
            "NUL",
            "COM1",
            "COM2",
            "COM3",
            "COM4",
            "LPT1",
            "LPT2",
            "LPT3",
            "CLOCK$",
        ]
        if filename.upper().startswith(tuple(reserved_names)):
            return False

        if filename.rstrip().endswith(".") or " " in filename:
            return False

        return True

    def dirChoose(self):
        self.directory = filedialog.askdirectory(title="Choose a Folder with Cards")
        for filename in sorted(os.listdir(self.directory)):
            if (
                filename.endswith(".png")
                or filename.endswith(".jpg")
                or filename.endswith(".jpeg")
            ):
                img = Image.open(os.path.join(self.directory, filename))
                self.imgs.append(img)

    def columnChoose(self):
        self.num_cols = 1
        while True:
            self.num_cols: str = qr.text("Enter the number of columns: ").ask()
            if self.num_cols is not None and self.num_cols.isdigit() == True:
                self.num_cols = int(self.num_cols)
                break
            else:
                print("Invalid input! Please try again")

        self.num_rows = (len(self.imgs) + self.num_cols - 1) // self.num_cols
        assert self.num_cols * self.num_rows == len(
            self.imgs
        ), "Number of rows and columns does not match the number of images in the folder"

    def resource_path(self, relative_path):
        # Get absolute path to resource, works for dev and for PyInstaller
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def horizontalGrid(self):
        gridHeight = IMG_HEIGHT * self.num_rows
        gridWidth = IMG_WIDTH * self.num_cols
        grid = Image.new("RGBA", (gridWidth, gridHeight), (255, 0, 0, 0))

        customNameBool = qr.confirm(
            "Would you like to choose a custom name for the horizontal grid?", default=False
        ).ask()
        if customNameBool:
            while True:
                customName = qr.text("Enter the name for the grid").ask()
                if self.isValid(customName):
                    break
                else:
                    print("Invalid filename!")
        else:
            customName = "Grid-Horizontal.png"

        qr.print("Plotting Horizontal Grid now...", style="bold fg:yellow")
        for i, img in enumerate(self.imgs):
            rowNum = i // self.num_cols
            colNum = i % self.num_cols
            x = IMG_WIDTH * colNum
            y = IMG_HEIGHT * rowNum
            try:
                grid.paste(img, (x, y))
            except Exception as e:
                print(f"Failed to place image at row {rowNum + 1}, column {colNum + 1}")
                exit(-1)
            else:
                print("Image {:02d} successfully plotted!".format(i + 1))

        qr.print(
            "Horizontal Grid successfully generated\n", style="bold italic fg:green"
        )
        grid.save(customName + ".png")

    def verticalGrid(self):
        gridHeight = (
            IMG_HEIGHT * self.num_rows + PADDING * (self.num_cols - 1) + BRDR_HEIGHT * 2
        )
        gridWidth = IMG_WIDTH * self.num_cols

        customNameBool = qr.confirm(
            "Would you like to choose a custom name for the vertical grid?", default=False
        ).ask()
        if customNameBool:
            while True:
                customName = qr.text("Enter the name for the grid").ask()
                if self.isValid(customName):
                    break
                else:
                    print("Invalid filename!")
        else:
            customName = "Grid-Vertical.png"

        qr.print("Plotting Slanted Grid now...", style="bold fg:yellow")

        grid = Image.new("RGBA", (gridWidth, gridHeight), (255, 0, 0, 0))
        border = Image.open(self.borderName)

        # This loop places the white borders on the top and the bottom of the grid
        for i in range(len(self.imgs)):
            colNum = i % self.num_cols
            x = IMG_WIDTH * colNum
            y = PADDING * (self.num_cols - (colNum + 1))
            try:
                grid.paste(border, (x, y))
            except Exception as e:
                print(f"Failed to place top border for column {colNum+1}!")
                input()
                exit(-1)
            y = gridHeight - BRDR_HEIGHT - PADDING * (colNum)
            try:
                grid.paste(border, (x, y))
            except Exception as e:
                print(f"Failed to place bottom border for column {colNum+1}")
                input()
                exit(-1)

        # Places the image at their respective positions
        for i, image in enumerate(self.imgs):
            rowNum = i // self.num_cols
            colNum = i % self.num_cols
            x = IMG_WIDTH * colNum
            y = (
                IMG_HEIGHT * rowNum
                + PADDING * (self.num_cols - colNum - 1)
                + BRDR_HEIGHT
            )
            try:
                grid.paste(image, (x, y))
            except Exception as e:
                print(f"Failed to plot image at row {rowNum+1}, column {colNum + 1}")
                input()
                exit(-1)
            else:
                print("Image {:02d} successfully plotted!".format(i + 1))

        qr.print(
            "Vertiical Grid successfully generated\n", style="bold italic fg:green"
        )
        grid.save(f"{customName}.png")


if __name__ == "__main__":
    app = Grid()
