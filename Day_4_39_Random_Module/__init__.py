import random  # import random module
import my_module  # import my custom-made module

# Generate a random int from 1 to 10.
random_integer = random.randint(1, 10)
print(random_integer)

# Access pi variable from my_module class.
print(my_module.pi)

# Generate a random float from 0 to 5.
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
