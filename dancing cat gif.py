import imageio.v3 as iio
import os
os.chdir(os.path.dirname(__file__)) 
filenames = ['H:/dancing cat/frame-1.png', 'H:/dancing cat/frame-2.png', 'H:/dancing cat/frame-3.png', 'H:/dancing cat/frame-2.png']

images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('dancing_cat.gif', images, duration = 500, loop = 0)