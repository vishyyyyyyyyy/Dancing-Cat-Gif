# 🕺🐱 Dancing Cat GIF Project

This project creates an animated GIF of a dancing cat using Python's `imageio` library. It was a fun and simple introduction to working with image processing and file manipulation in Python.

## 📌 What I Learned

- How to use the `imageio` module, especially the `imwrite()` function, to create GIFs.
- How to use the `os` module to change the working directory to the script’s location.
- How to work with lists in Python, including appending images to a list before writing them to a file.
- Some basic troubleshooting related to transparent backgrounds in image sequences and how they can cause frames to overlap if not handled properly.

## 🧠 Project Notes

Originally, I tried to make the GIF with a transparent background, but the frames would stack instead of clearing between each image. As a workaround, I added a solid background to each frame. I plan to revisit the transparency issue and find a better solution in the future.

## 🧪 How It Works

```python
import imageio.v3 as iio
import os

# Set working directory to current script location
os.chdir(os.path.dirname(__file__))

# List of frame file paths
filenames = [
    'H:/dancing cat/frame-1.png',
    'H:/dancing cat/frame-2.png',
    'H:/dancing cat/frame-3.png',
    'H:/dancing cat/frame-2.png'
]

# Read images into a list
images = []
for filename in filenames:
    images.append(iio.imread(filename))

# Write images to a looping GIF
iio.imwrite('dancing_cat.gif', images, duration=500, loop=0)
