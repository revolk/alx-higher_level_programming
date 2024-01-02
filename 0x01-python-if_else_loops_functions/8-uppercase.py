#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter (ASCII values 97 to 122)
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase by subtracting 32 from its ASCII value
            uppercase_char = chr(ord(char) - 32)
        else:
            # Keep non-letter characters unchanged
            uppercase_char = char
        print(uppercase_char, end="")
    print()  # Print a newline at the end

# Test the function with example strings
uppercase("best")
uppercase("Best School 98 Battery street")

