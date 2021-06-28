# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Combine the name, make them into lower case.
name = name1.lower() + name2.lower()
score1 = 0  # TRUE score
score2 = 0  # LOVE score

score1 = name.count('t') + name.count('r') + name.count('u') + name.count('e')
score2 = name.count('l') + name.count('o') + name.count('v') + name.count('e')

# Convert the scores to String, combine them, then convert the final score back to int.
finalScore = int(str(score1) + str(score2))

if finalScore < 10 or finalScore > 90:
    print(f"Your score is {finalScore}, you go together like coke and mentos.  ")
elif 40 <= finalScore <= 50:
    print(f"Your score is {finalScore}, you are alright together.  ")
else:
    print(f"Your score is {finalScore}.  ")
