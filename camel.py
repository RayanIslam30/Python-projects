#Code that takes a camel case string and converts it to snake case

#Gets user input for a camel case string and converts it to snake case using the camel_to_snake function
def main(): 
    camel_str = input("Enter a camel case string: ")
    snake_str = camel_to_snake(camel_str)
    print("Snake case string:", snake_str)

#Converts from camel to snake by changing uppercase letters to lowercase and adding an underscore before them
def camel_to_snake(camel_str):
    snake_str = ''
    for char in camel_str:
        if char.isupper():
            snake_str += '_' + char.lower()
        else:
            snake_str += char
    return snake_str.lstrip('_')
main()
