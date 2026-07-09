#Code to take two integers and either add, subtract, multiply or divide them based on user input

user_input = input("Enter your equation, with a space between each number and operator: ") #Take the input from the user
x, y, z = user_input.split()
x = float(x)
z = float(z)

#ifelse statement to check the operator and perform the corresponding operation
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("Invalid operator. Please use +, -, *, or /")