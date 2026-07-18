#Code that takes a csv file with two parameters, and gives it three parameters instead, putting the three parameter data in a new csv file

import sys #Import sys to use sys.argv and take system arguments
import csv #Import csv module to work with our csv files

#Check that sys.argv[1] and sys.argv[2] exists
if len(sys.argv) == 3: #If file is valid, set name variable to file name
    name = sys.argv[1] #set our file name to file user inputted
    output = sys.argv[2] #set our new file to write
elif len(sys.argv) < 3: #If sys.argv[1] or [2] doesn't exist, quit with too few arguments
    sys.exit("Too few command-line arguments")
else: #If there are more than 2 arguments, quit with too many arguments
    sys.exit("Too many command-line arguments")

#Make sure the file is actually a .csv file, otherwise quit
if not name.endswith(".csv"):
    sys.exit("Not a CSV file")

#If those checks pass, then try and read the csv file
try:
    with open(name) as file:
        reader = csv.DictReader(file) #use dictionary reader to read the key on the top row of csv file 
        for row in reader:
            last, first = row["name"].split(",")
            first = first.strip()
            print(first, last, row["house"])
except FileNotFoundError:
    sys.exit("File does not exist")

