#Code that takes a fraction and converts to a percentage, similar to how a fuel gauge works. Also returns F on high percentage and E on low percentage

def main():
    #Keep asking for fraction until user gives valid one
    while True:
        try:
           fraction = input("Fraction: ")
           percentage = convert(fraction)
           break
        except (ValueError, ZeroDivisionError):
           pass
    #Print out percentage
    fuel = gauge(percentage) 
    print(fuel)

#Function to convert fraction to percentage, catching user error in input
def convert(fraction):
    x, y = fraction.split("/") 
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x < 0 or x > y:
        raise ValueError

    return x / y * 100


#Returns the appropriate gauge reading
def gauge(percentage):
    if percentage >= 99:
        return "F" 
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__": #Only run main if file ran directly
    main()

