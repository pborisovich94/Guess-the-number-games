import random

required_number = random.randrange(1000) # Stores a random number from 0 to 1000

entered_number = -1 # -1 to avoid matching a required_number variable
attempts = 0      

while entered_number != required_number:
    entered_number = int(input("Enter the number:  ")) # Ask user to enter a number
    attempts += 1 # Increases the attempt counter by 1
    
    if entered_number > required_number:
        print("The guessed number is less!")
    elif entered_number < required_number:
        print("The guessed number is greater!")

print(f"\nYou guessed the number!\nThe number of your attempts is - {attempts}")