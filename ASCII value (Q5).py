# Function to print the ASCII value of a character
def print_ascii_value(character):
    ascii_value = ord(character)
    print(f"The ASCII value of '{character}' is {ascii_value}")

# Input from the user
char = input("Enter a character: ")
print_ascii_value(char)