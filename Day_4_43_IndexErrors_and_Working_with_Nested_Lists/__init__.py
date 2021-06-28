fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Place two lists inside another list, creating a nested list.
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# Should print Kale.  
print(dirty_dozen[1][1])
