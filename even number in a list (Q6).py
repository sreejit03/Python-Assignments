# Function to print even numbers in a list
def print_even_numbers(numbers):
    # Iterate over each number in the list
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            # Print the even number
            print(num)

# Example list of numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function with the example list
print_even_numbers(numbers_list)