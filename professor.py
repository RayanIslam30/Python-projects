#Code that allows the user to choose between 3 levels, and solve 10 random math problems for that level. Mimicks the educational toy 'little professor'

import random #Import random module to get random numbers 

def main():
    level = get_level() 
    score = int(0) #Initialize our points counter
#Ask our 10 questions 
    for _ in range(10):
        #Get random integers
        x = generate_integer(level)
        y = generate_integer(level)

    #Give user the question, they have three chances to get it right
        for _ in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
            if guess == x + y:
                score += 1
                break
            else:
                print("EEE")
    print(f"Score: {score}")

#Function to get our level
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            # User chooses a level, either 1, 2, or 3
            if level in [1,2,3]:
                return level
        except ValueError:
            pass


#Function to generate random numbers based on level
def generate_integer(level):
    if level == 1: #Level 1, single-digit numbers
        int = random.randint(0,9)
        return int
    elif level == 2: #Level 2, double-digit numbers
        int = random.randint(10,99)
        return int
    else: #otherwise must be level 3, triple-digit numbers
        int = random.randint(100,999)
        return int

if __name__ == "__main__":
    main() 