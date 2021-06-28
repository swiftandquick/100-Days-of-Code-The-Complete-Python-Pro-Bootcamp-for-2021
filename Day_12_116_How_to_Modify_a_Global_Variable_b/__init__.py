# Modifying global scope.

enemies = 1


def increase_enemies():
    # Prints 1.
    print(f"Enemies inside function:  {enemies}.  ")
    return enemies + 1


# Increment enemies (global variables) by 1.
enemies = increase_enemies()
# Prints 2.
print(f"Enemies inside function:  {enemies}.  ")