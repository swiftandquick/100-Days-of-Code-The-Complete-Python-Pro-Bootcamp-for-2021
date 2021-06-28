# Write your code below this line 👇

import math


def prime_checker(number):
    prime = True
    if number <= 1:
        prime = False
    for divisor in range(2, math.ceil(math.sqrt(number + 1))):
        if (number % divisor == 0):
            prime = False
    if prime:
        print("It's a prime number.  ")
    else:
        print("It's not a prime number.  ")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
