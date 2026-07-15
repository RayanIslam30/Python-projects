#Code that allows the user to order from a taqueria menu and calculates the total cost of the order, incrementing the total cost as items are added to the order.

#This is a dictionary that contains the menu items and their corresponding prices. The keys are the names of the menu items, and the values are the prices of those items.
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#This variable is used to keep track of the total cost of the order. It is initialized to 0.0 at the beginning of the program.
total = 0.0
#While loop that allows the user to order multiple items from the menu until they choose to quit by by inputting ctrl-d
while True:
    try: 
        order = input("Enter an item to order: ").strip().title() #Takes and cleans user input for a menu item, converting it to title case and removing any leading or trailing whitespace
        if order in menu:  
            total = menu[order] + total #Checks if the ordered item is in the menu dictionary and adds the price of that item to the total cost if it is
            print(f"Total: ${total:.2f}") #Prints out the total cost of the order, formatted to two decimal places
    except EOFError: #if user inputs ctrl-d, the program will exit the loop and end the program
        break

