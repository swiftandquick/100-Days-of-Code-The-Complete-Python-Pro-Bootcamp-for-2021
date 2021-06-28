print("Welcome to Treasure Island")
print("Your mission is to find the treasure.  ")

direction = input("You're at a cross road.  Where do you want to go?  Type 'left' or 'right'.  ")
if direction.lower() == "left":
    wait_or_swim = input("You come to a lake.  There is an island in the middle of the lake.  Type 'wait' to wait "
                         "for a boat.  Type 'swim' to swim across.  ")
    if wait_or_swim.lower() == "wait":
        door = input("You arrive at the island unharmed.  There is a house with 3 doors.  One red, one yellow, "
                     "and one blue. Which color do you choose?  ")
        if door.lower() == "yellow":
            print("You win!  ")
        else:
            print("You enter a room of beasts.  Game over.  ")
    else:
        print("You got attacked by an angry trout.  Game over.  ")
else:
    print("You fell into a hole.  Game over.  ")
