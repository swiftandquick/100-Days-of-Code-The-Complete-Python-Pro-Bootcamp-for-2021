# Round the result of 8 /3 to 2 decimal places.
print(round(8 / 3, 2))

# Floor division, round to integer (floor), result is 2.
print(8 // 3)

# Floor division always result in int type.
print(type(8 // 3))

# Regular division always result in float type.
print(type(4 / 2))

score = 0
height = 1.8
isWinning = True

# Use f-String to print without concatenation or conversion.
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
