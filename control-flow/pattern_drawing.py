# pattern_drawing.py

# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Validate the input
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through each row
    row = 0
    while row < size:
        # Use a for loop to print asterisks for each column in the row
        for col in range(size):
            print("*", end="")  # Print without advancing to a new line
        print()  # Move to the next line after each row
        row += 1

