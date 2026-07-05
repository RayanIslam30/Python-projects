#Code to calculate the tip based on the meal cost and tip percentage

#our main function to prompt user for cost of meal and tip percentage, then calculate and print the tip amount
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#function to convert dollars input to float
def dollars_to_float(d):
    d=d.replace("$","") #remove the dollar sign, if there is one
    return float(d) #convert to float

#function to convert percentage input to float
def percent_to_float(p):
    p=p.replace("%","") #remove the percentage sign, if there is one
    return float(p)/100 #convert to float and divide by 100 to get the decimal value


main()