# Scope

enemies = 1


def increase_enemies():
    enemies = 2
    # Prints 2 because local variable is 2.
    print(f"enemies inside function:  {enemies}")


increase_enemies()
# Prints 1 because global variables is 1, global variable enemies is not the same as local variables.
print(f"enemies outside function:  {enemies}")


# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# potion_strength is a local variable, can't be used outside of drink_potion() function.
# print(potion_strength)


# Global Scope

player_health = 10


def drink_potion():
    potion_strength = 2
    # player_health has global scope, so it can be used inside drink_potion().
    print(player_health)


drink_potion()
