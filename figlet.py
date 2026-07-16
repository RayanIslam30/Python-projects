#Code to take ordinary letters and convert them to large, block-like form, using pre-exisiting library
import sys #Import sys so that we can use it later
import random #Import random so we can randomly call font later
from pyfiglet import Figlet #Import library which converts our normal input to large letters
figlet = Figlet()

text = input("Input: ") #Get user input to prepare for converting 
#Two cases to account for. User can either choose the font they want, or leave it random
if len(sys.argv) == 3: #Check if user specified a font while running program
        if sys.argv[1] not in ["-f", "--font"]: #If user didn't call font, quit
            sys.exit("Invalid usage")
        elif sys.argv[2] not in figlet.getFonts(): #If the font isn't valid, quit
            sys.exit("Invalid usage")
        else: #Valid font, use that font and output text
            figlet.setFont(font=sys.argv[2]) #set font to user specified font
            print(figlet.renderText(text)) #print figlet
elif len(sys.argv) == 1: #User only inputted text, leave font random
        randomfont = random.choice(figlet.getFonts()) #get a random font
        figlet.setFont(font=randomfont) #set the random font
        print(figlet.renderText(text)) #print figlet 
else:
        sys.exit("Invalid usage")

    