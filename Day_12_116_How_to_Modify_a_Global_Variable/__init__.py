# Modifying global scope.

enemies = 1


def increase_enemies():
    # Use global keyword to define enemies as a global variable.
    global enemies
    # This enemies value is a global variable.
    enemies += 1
    print(f"Enemies inside function:  {enemies}.  ")


increase_enemies()
# This will also print 2, when a global variable is modified within a function, it changes globally.
print(f"Enemies inside function:  {enemies}.  ")