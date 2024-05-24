def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    """Print all prime numbers in the interval from start to end (inclusive)."""
    for number in range(start, end + 1):
        if is_prime(number):
            print(number)

# Get user input for the interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Print all prime numbers in the given interval
print(f"Prime numbers between {start} and {end} are:")
print_primes_in_interval(start, end)