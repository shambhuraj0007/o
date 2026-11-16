
# Function to calculate Fibonacci number recursively
def fibonacci_recursive(n):

    # Base condition to stop recursion
    if n <= 1:
        return n  # Return 0 or 1

    # Calculate Fibonacci using recursive calls
    return (fibonacci_recursive(n - 1)
            + fibonacci_recursive(n - 2))

# Accept number of terms from the user
n = int(input("Enter number of terms: "))

# Display the series heading
print("Fibonacci Series (Recursive):")

# Generate and print Fibonacci numbers
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
