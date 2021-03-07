#!/usr/bin/env python3
import PIL

#folder
~/images
from PIL import Image
#Iterate through each file in the folder
for file in images

#For each file:
#  Rotate the image 90° clockwise
#  Resize the image from 192x192 to 128x128
#  Save the image to in the folder: /opt/icons/ in .jpeg format
im.rotate(90).resize((128,128)).save("flipped_and_resized.jpg")
