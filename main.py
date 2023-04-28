import urllib.request
from PIL import Image
import tkinter as tk
import os

from tkinter import filedialog, simpledialog

root = tk.Tk()
root.withdraw()

imgs = []
directory = filedialog.askdirectory(mustexist=True,title="Choose a folder with cards")

for filename in sorted(os.listdir(directory)):
    if filename.endswith(".png"):
        img = Image.open(os.path.join(directory, filename))
        imgs.append(img)

# dimensions of the base image
imgHeight = 800
imgWidth = 600

# Ask the user for the no. of columns in the grid and automatically calculate the no. of rows.
while True:
    num_cols = simpledialog.askinteger("Columns", "Enter the number of columns:")
    if num_cols is not None and type(num_cols) == int:
        break
    else:
        print("Invalid input. Please enter a whole number.")

num_rows = (len(imgs) + num_cols - 1) // num_cols

# Fetches and stores the border in the same location as the .exe file
borderURL = "https://i.imgur.com/AMBdG9m.png"
filename = "border.png"

with urllib.request.urlopen(borderURL) as response, open(filename, "wb") as out_file:
    data = response.read()
    out_file.write(data)


border = Image.open(filename)

# Checks if the number of columns is suitable to generate a grid. If not, program is exited automatically
assert num_cols * num_rows == len(
    imgs
), "Number of rows and columns must match the number of images!"

# This accounts for the slant of the grid as well as the white borders which are to be placed on top

grdHght = imgHeight * num_rows + 121 * (num_cols - 1) + 310
grdWdth = imgWidth * num_cols

grid = Image.new("RGBA", (grdWdth, grdHght), (255, 0, 0, 0))

# Used to place the white borders on top and bottom
for i in range(len(imgs)):
    col = i % num_cols
    x = imgWidth * col
    y = 121 * (num_cols - (col + 1))
    grid.paste(border, (x, y))
    y = grdHght - 155 - 121 * (col)
    grid.paste(border, (x, y))

# Placement of images/cards
for i, img in enumerate(imgs):
    row = i // num_cols
    col = i % num_cols
    x = imgWidth * col
    y = imgHeight * row + 121 * (num_cols - col - 1) + 155
    grid.paste(img, (x, y))
    print(f"Image {i+1} plotted successfully!")

#saving of the grid
grid.save("grid.png")
