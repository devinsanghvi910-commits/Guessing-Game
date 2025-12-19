import random

print("Hello, Welcome to the Guessing Game!")
print("You have 3 guesses to guess a number between 1 and 10! Good Luck")
secret_number = random.randint(1, 10)
count = 0
while count < 3:
    guess = int(input('Guess: '))
    if guess == secret_number:
        print('You guessed the number!')
        exit(0)
    else:
        print('Wrong! Try again!')
        count += 1
print(f"Guesses up! Try again next time. The number was {secret_number}")