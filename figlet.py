#Code to take ordinary letters and convert them to large, block-like form, using pre-exisiting library
import sys #Import sys so that we can use it later
from pyfiglet import Figlet #Import library which converts our normal input to large letters
figlet = Figlet()

text = input("Input: ") #Get user input to prepare for converting 

#Two cases to account for. User can either choose the font they want, or leave it random
if len(sys.argv) == 3: #Check if user chose font. 3 arguments because 1 for text, 1 for calling font, 1 for font name
    if sys.argv[1] not in ["-f", "--font"]: #If user didn't call font, quit
        sys.exit("Invalid usage")
    elif sys.argv[2] not in figlet.getfonts(): #If the font isn't valid, quit
        sys.exit("Invalid usage")
    else: #Valid font, use that font and output text

elif len(sys.argv) == 1 #User only inputted text, leave font random
    