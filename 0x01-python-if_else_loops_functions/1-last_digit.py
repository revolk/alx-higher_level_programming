#!/usr/bin/python3
import random

# This line should not change
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
last_digit = abs(number) % 10

# Print the result
print(f"Last digit of {number} is {last_digit}", end=" ")

# Check conditions for the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

