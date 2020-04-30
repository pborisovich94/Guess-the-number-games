import time

# Game settings
a = 0    # Number from
b = 1000 # NUmber to

# The function that displays the rules of the game
def print_rules():
    rules = "\nIf I guess, then enter \"=\"\nIf your number is less, then enter \"<\"\nIf your number is greater, then enter \">\"\n"
    print(rules)

# Before guessing the number, with an interval of 1 second, we display messages for the user
print(f'Guess the number from {a} to {b}...')
time.sleep(1)
print('Done?')
time.sleep(1)
print('Let`s go!')
time.sleep(1)
print_rules()
time.sleep(1)

attempts = 0 # Attempts counter

while True:
    # Check that the number "from" is not greater than the number "to"
    if a > b:
        print('Number \"from\" cannot be greater than a number \"to\"!')
        print('Edits required')
        break
    
    if a == b:
        print(f'Got it. The answer is - {a}')
        print(f'It took {attempts} attempts')
        break

    attempts += 1

    number = (a + b) // 2
    answer = input(f'The number is {number}? ')

    if answer == '=':
        print('\nWoohoo! I guessed right!')
        print(f'It took {attempts} attempts')
        break
    elif answer == '<':
        b = number - 1
    elif answer == '>':
        a = number + 1
    else:
        print('I don`t understand. Just in case, I remind you the rules:')
        print_rules()
        attempts -= 1