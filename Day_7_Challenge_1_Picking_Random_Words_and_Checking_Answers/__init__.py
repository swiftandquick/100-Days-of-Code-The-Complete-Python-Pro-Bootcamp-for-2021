import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_word = random.choice(word_list)
print(random_word)

# Make the word into a list of characters.
word_letters = list(random_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess the letter:  ").lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

def check_letter(guess, word_letters):
    for letter in word_letters:
        if guess == letter:
            return True
    return False


letter_in_word = check_letter(guess, word_letters)
if letter_in_word:
    print("Letter is in word.  ")
else:
    print("Letter is not in word.  ")
