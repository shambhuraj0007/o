# EXPERIMENT 1: FIBONACCI SERIES USING RECURSIVE AND NON-RECURSIVE METHODS

# Function to generate Fibonacci series using iteration
def fibonacci_iterative(n):
    a = 0  # Store the first Fibonacci number
    b = 1  # Store the second Fibonacci number

    for i in range(n):  # Repeat the loop n times
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Update a and b for the next term


# Function to calculate one Fibonacci number using recursion
def fibonacci_recursive(n):
    if n <= 1:  # Check the base condition
        return n  # Return 0 or 1 when the base condition is reached

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)  # Add the previous two terms


# Accept the number of terms from the user
n = int(input("Enter number of terms: "))

# Check whether the entered number is valid
if n < 0:
    print("Please enter a non-negative number.")
else:
    # Display the iterative Fibonacci series
    print("Fibonacci Series (Non-Recursive):")
    fibonacci_iterative(n)

    # Display the recursive Fibonacci series
    print("\nFibonacci Series (Recursive):")
    for i in range(n):  # Generate terms from position 0 to n-1
        print(fibonacci_recursive(i), end=" ")  # Calculate and print each term
    print()  # Move to the next line
