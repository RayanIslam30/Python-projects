#Code that takes 2 images, and overlays one on top of the other
#In my case, it will be used to overlay Harvards 'I took CS50' shirt onto my cat

import sys #Import sys to use sys.argv and take system arguments
import os #Import os to check file extensions
from PIL import Image, ImageOps #Import image opening and resizing/cropping 

#Check that sys.argv[1] and sys.argv[2] exists
if len(sys.argv) == 3: #If file is valid, set name variable to file name
    name = sys.argv[1] #set our file name to file user inputted
    output = sys.argv[2] #set our new file to write
elif len(sys.argv) < 3: #If sys.argv[1] or [2] doesn't exist, quit with too few arguments
    sys.exit("Too few command-line arguments")
else: #If there are more than 2 arguments, quit with too many arguments
    sys.exit("Too many command-line arguments")
