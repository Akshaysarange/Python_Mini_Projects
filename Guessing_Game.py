import random

easy_level = ['apple', 'train', 'tiger', 'money', 'india']
medium_level = ["python", 'bottle', 'monkey', 'planet', 'laptop']
hard_level = ['elephant', 'diamond', 'umbrella', 'computer', 'mountain']

print('Welcome to the Guessing game')
print('Choose a difficulty level: Easy, Medium, Hard')

level = input('Enter difficulty :- ').lower()

if level == 'easy':
    secret = random.choice(easy_level)
elif level == 'medium':
    secret = random.choice(medium_level)
elif level == 'hard':
    secret = random.choice(hard_level)
else:
    print('Invalid choice, Defaulting to easy level')
    secret = random.choice(easy_level)

attempts = 0
print('\nGuess the secret word')

while True:
    guess = input('Enter your guess:- ').lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulations! You guessed it in {attempts} attempts')
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint: ", hint)

print("GAME OVER!!!")