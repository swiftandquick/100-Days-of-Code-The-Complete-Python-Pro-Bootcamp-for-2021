print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?  "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!  ")
    age = int(input("What is your age?  "))
    # Nested conditional statement, conditional statement inside conditional statement.
    if age < 12:
        bill = 5
        print("Child tickets are $5.  ")
    elif 12 <= age <= 18:
        bill = 7
        print("Youth tickets are $5.  ")
    else:
        bill = 12
        print("Adult tickets are $12.  ")

    wants_photo = input("Do you want a photo taken?  Y or N.  ")
    if wants_photo == "Y":
        # Add $3 bills to their bill.
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.  ")
