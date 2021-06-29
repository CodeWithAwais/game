import random


amount = int(input("Enter the amount of money you wants to insert into the slow machin: "))
fruits = ["Mangoes", "Banana", "Oranges", "Peach", "Grapes", "Apple", "Berries"]

while True:
    matched = []
    for i in range(3):
        random_fruit = random.choice(fruits)
        print(random_fruit)

        matched.append(random_fruit)
    
    unique_fruits = len(set(matched))
    if unique_fruits == 3:
        print("You won RS: 0")
    if unique_fruits == 2:
        print(f"You have won RS: {amount + amount}")
    if unique_fruits == 1:
        print(f"You have won RS: {amount + amount + amount}")
    else:
        play_again = input("Do you want to play again [Yes/No]: ")
        if play_again.lower() == 'yes':
            continue

        if play_again.lower() == 'no':
            break
        else:
            print("You typed a wrong answer. Only choose between \"yes\" or \"No\"")
            print("Restart the game... ")
            break
