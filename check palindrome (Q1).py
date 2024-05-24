def is_armstrong_number(number):
    # Convert the number to a string to easily iterate through each digit
    str_num = str(number)
    # Get the number of digits
    num_digits = len(str_num)
    # Calculate the sum of the digits each raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Get user input
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")