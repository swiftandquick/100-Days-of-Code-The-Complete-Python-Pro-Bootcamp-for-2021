# Function takes f_name and l_name as arguments.
def format_name(f_name, l_name):
    # Early return, if there is no input for first name or last name, return a message instead.
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs.  "
    # title() capitalize first letter of every word, but other letters are in lower case.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # Return a String.
    return f"{formated_f_name} {formated_l_name}"


# Print out the returned value of the format_name function.
print(format_name(input("What is your first name?  "), input("What is your last name?  ")))
