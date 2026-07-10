#Code to simulate a vending machine that will dispense a drink when user inputs the correct amount of money, and will return change if the user inputs more than the cost of the drink


def main():
    #define our variables for the cost of the drink and the amount of money inserted by the user
    drink_cost = int(50)
    money_inserted = int(0)
    # Check if the user has inserted enough money
    while money_inserted < drink_cost:
        print(f"Amount Due: {drink_cost - money_inserted}")
        money = int(input("Insert Coin:"))
        #Check if the user has inserted a valid coin (5, 10, or 25 cents)
        if money not in (5,10,25):
            print("Invalid coin. Please insert a valid coin.")
        #If the user has inserted a valid coin, add it to the total amount of money inserted
        else:
            money_inserted += money
    else:
        # Calculate change to return
        change = money_inserted - drink_cost
        print(f"Change Owed: {change}")

main()