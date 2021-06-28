from art import logo
print(logo)

first_number = int(input("What is the first number?:  "))

keep_going = "y"
first_iteration = True

while keep_going == "y" or keep_going == "n":

    def continue_operation(number):
        operator = input("+\n-\n*\n/\nPick an operation:  ")
        second_number = float(input("What's the next number?:  "))
        if operator == "+":
            result = first_number + second_number
            print(f"{first_number} + {second_number} = {result}")
            return result
        elif operator == "-":
            result = first_number - second_number
            print(f"{first_number} - {second_number} = {result}")
            return result
        elif operator == "*":
            result = first_number * second_number
            print(f"{first_number} * {second_number} = {result}")
            return result
        elif operator == "/":
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result}")
            return result
        else:
            return

    if not first_iteration:
        keep_going = input(
            f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation:  ")

    first_iteration = False

    if keep_going == "y":
        first_number = continue_operation(first_number)
    elif keep_going == "n":
        first_number = float(input("What is the first number?:  "))
        first_number = continue_operation(first_number)
    else:
        print("Invalid input, exit calculator.  ")
