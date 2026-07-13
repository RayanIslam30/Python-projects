#Code that takes a fraction and converts to a percentage, similar to how a fuel gauge works. Also returns F on high percentage and E on low percentage

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    gauge(percentage)

#Converts the fraction to a percentage
def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if (x/y) > 1 or (x/y) < 0: #If the fraction is greater than 1 or negative, raise a ValueError
            raise ValueError
        return (x / y) * 100
    except (ValueError, ZeroDivisionError): #If an exception is raised, the program will ask for a fraction again
        return convert(input("Fraction: "))

#Returns the appropriate gauge reading
def gauge(percentage):
    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage:.0f}%")

main()