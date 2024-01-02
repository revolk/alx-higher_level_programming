#!/usr/bin/python3
# Start the loop from the ASCII value of 'a' (97) to 'z' (122)
for char in range(ord('a'), ord('z') + 1):
    # Use the 'end' parameter to avoid a newline character after each print
    print(chr(char), end='')

# Print a newline character at the end to complete the output
print()

