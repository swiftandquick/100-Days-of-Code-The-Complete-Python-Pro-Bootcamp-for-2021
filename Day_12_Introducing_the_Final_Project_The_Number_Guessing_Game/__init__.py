import random

print("Welcome to the Number Guessing Game!  ")
print("I'm thinking of a number between 1 and 100.  ")

secret = random.randint(1, 100)

difficulty = input("Choose a difficulty.  Type 'easy' or 'hard':  ").lower()

if difficulty == "easy":
    tries = 10
elif difficulty == "hard":
    tries = 5
else:
    tries = 0


def guess(attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.  ")
        n = int(input("Make a guess:  "))
        if n > secret:
            print("Too high.  ")
            attempts -= 1
        elif n < secret:
            print("Too low.  ")
            attempts -= 1
        else:
            return f"You got it!  The answer is {secret}.  "
        if attempts >= 2:
            print("Guess again.  ")
    return "You've run out of guesses, you lose.  "


print(guess(tries))
