#!/usr/bin/python3
# Use two nested loops to iterate through all possible pairs of digits
for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        # Use string formatting to print the two digits with leading zeros if necessary
        print(f"{first_digit}{second_digit}", end=", " if first_digit != 8 or second_digit != 9 else "\n")

