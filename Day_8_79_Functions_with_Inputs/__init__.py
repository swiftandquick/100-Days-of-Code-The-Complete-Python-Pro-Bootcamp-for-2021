# Function without input.
def greet():
    print("Hello.  ")
    print("How do you do?  ")
    print("Isn't the weather nice today?  ")


# Call the greet() function.
greet()


# Function that allows arguments, the parameter is name, the argument is "Billie", so name = "Billie".
def greet_with_name(name):
    print(f"Hello {name}.  ")
    print(f"How do you do {name}?")


# Call the greet_with_name function, pass "Billie" as argument.
greet_with_name("Billie")
