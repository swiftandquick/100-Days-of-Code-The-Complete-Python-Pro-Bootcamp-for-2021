# Function takes f_name and l_name as arguments.
def format_name(f_name, l_name):
    # title() capitalize first letter of every word, but other letters are in lower case.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # Return a String.
    return f"{formated_f_name} {formated_l_name}"


# Print out the returned value of the format_name function.
print(format_name("AnGElA", "YU"))
