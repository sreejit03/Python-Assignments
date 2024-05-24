def fibonacci(n):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def main():
    try:
        n = int(input("Enter the position of the Fibonacci number you want: "))
        result = fibonacci(n)
        print(f"The {n}-th Fibonacci number is: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()