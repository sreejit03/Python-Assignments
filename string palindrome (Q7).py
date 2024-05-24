def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(filter(str.isalnum, s)).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')