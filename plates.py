#Code that checks if a string is valid for a vanity license plate

def main():
    plate = input("Enter a vanity license plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    #Checks if the plate is valid by checking the length, allowed characters, and format
    if len(plate) < 2 or len(plate) > 6:
        return False
    if not plate.isalnum(): #Checks if the plate contains only letters and numbers
        return False
    if plate[0].isalpha() == False or plate[1].isalpha() == False: #Checks if the first two characters are letters
        return False
    if plate[0] == '0': #Checks if the first number is 0
        return False
    if any(char.isdigit() for char in plate[:-1]) and not plate[-1].isdigit(): #Checks if there are any digits in the plate except for the last character, and if the last character is not a digit
        return False
    return True

main()