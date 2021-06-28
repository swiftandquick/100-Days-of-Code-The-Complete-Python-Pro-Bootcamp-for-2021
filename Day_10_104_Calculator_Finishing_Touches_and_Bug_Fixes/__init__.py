# Calculator
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# The value of the dictionary items are functions.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?:  "))
    for symbol in operations:
        print(symbol)
    # Set should_continue as a flag, it's initially true, if it's set to False, calculator resets.
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above:  ")
        num2 = float(input("What's the next number?:  "))
        """ Set up calculation function based on operation symbol, if the symbol is "*", the function stored in 
        calculation_function is multiply().  """
        calculation_function = operations[operation_symbol]
        # Call the proper function to calculate the result.
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.:  ") == "y":
            num1 = answer
        else:
            should_continue = False
            # Recursion, calculator() function is called again.
            calculator()


calculator()
