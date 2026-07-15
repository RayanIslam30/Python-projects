#Code to take user input and add it to a grocery list, and record amount of times one item is inputted

#Initialize the grocery list as a dictionary, keys are groceries, values are amount of item.
grocery_list = {}

#While loop asks for user to keep inputting items for grocery list until user inputs ctrl-d
while True:
    try:
        item = input("Enter an item to add to your grocery list: ").upper() #Get user input for grocery list, put it all in uppercase 
        #if statement to figure out if item is already in list, and if it is, just add to amount
        if item in grocery_list:
            grocery_list[item] += 1 #Add one to the item count
        else:
            grocery_list[item] = 1 #Give item value of 1, add to list
    except EOFError:
        break

print("\nYour grocery list:")
for item in sorted(grocery_list): #Sorted list puts in alphabetical order
    print(grocery_list[item], item) #Prints out item and amount