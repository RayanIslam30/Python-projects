#Code that checks if a string is valid for a vanity license plate

def main():
    plate = input("Enter a vanity license plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Checks if the inputted plate meets all criteria for a valid vanity license plate, including length, allowed characters, and format
def is_valid(plate):
    #Checks if plate is valid length
    if len(plate) < 2 or len(plate) > 6:
        return False
    if not plate.isalnum(): #Checks if the plate contains only letters and numbers
        return False
    if not plate[0].isalpha() or not plate[1].isalpha(): #Checks if the first two characters are letters
        return False
    #Checks if the first number is 0
    for i in range(len(plate)):
        if plate[i].isdigit():
            if plate[i] == '0':
                return False
            break #Takes us out of the loop once we find the first number, only returns False if the first number is 0

    #Checks that after first number, all characters are numbers
    for i in range(len(plate)):
        if plate[i].isdigit():
            for j in range(i, len(plate)):
                if not plate[j].isdigit():
                    return False
            break #Takes us out of the loop, only returns false if any character after the first number is not a number

    return True #If all checks pass, the plate is valid

if __name__ == "__main__": #Only run main if file ran directly
    main()