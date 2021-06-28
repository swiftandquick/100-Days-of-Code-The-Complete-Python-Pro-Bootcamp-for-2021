print("Welcome to the tip calculator.  ")
totalBill = input("What was the total bill?  $")
tip = input("What percentage tip would you like to give?  10, 12, or 15?  ")
people = input("How many people to split the bill?  ")

costPerPerson = round(float(totalBill) * (1 + float(tip) / 100) / int(people), 2)
print(f"Each person should pay:  ${costPerPerson}")
