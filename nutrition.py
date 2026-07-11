#Code to take user input for a top 20 most consumed fruit and print out the amount of calories in that fruit

#A dictionary of fruits and their corresponding calorie counts
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 30,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

fruit = input("Enter a fruit: ").strip().lower()
if fruit in fruits:
    print(f"Calories: {fruits[fruit]}")