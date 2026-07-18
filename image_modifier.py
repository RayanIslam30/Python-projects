#Code that takes 2 images, and overlays one on top of the other
#In my case, it will be used to overlay Harvards 'I took CS50' shirt onto my cat

import sys #Import sys to use sys.argv and take system arguments
import os #Import os to check file extensions
from PIL import Image, ImageOps #Import image opening and resizing/cropping 

#Check that sys.argv[1] and sys.argv[2] exists
if len(sys.argv) == 3: #If file is valid, set name variable to file name
    input = sys.argv[1] #set image user wants modified
    output = sys.argv[2] #set location for new image
elif len(sys.argv) < 3: #If sys.argv[1] or [2] doesn't exist, quit with too few arguments
    sys.exit("Too few command-line arguments")
else: #If there are more than 2 arguments, quit with too many arguments
    sys.exit("Too many command-line arguments")
    
#Get our file endings to use for checks
input_ext = os.path.splitext(sys.argv[1])[1].lower() #Get file ending of original image
output_ext= os.path.splitext(sys.argv[2])[1].lower() #Get file ending of where the new image will be

if input_ext not in [".jpg", ".jpeg", ".png"] or output_ext not in [".jpg", ".jpeg", ".png"]: #Check that file endings are either jpg or png
    sys.exit("Invalid input")

if input_ext != output_ext: #If input ending is not equal to output ending, quit
    sys.exit("Input and output have different extensions")

#If all those checks passed, start the overlay process
shirt = Image.open("images/shirt.png") #Get the shirt image from images folder

