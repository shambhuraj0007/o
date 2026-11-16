
# Function to generate Fibonacci series
def fibonacci_iterative(n):

    a = 0  # First Fibonacci number
    b = 1  # Second Fibonacci number stored

    # Repeat the loop n times
    for i in range(n):

        print(a, end=" ")  # Print current Fibonacci number

        a, b = b, a + b  # Update the two numbers

# Accept number of terms from the user
n = int(input("Enter number of terms: "))

# Display the series heading
print("Fibonacci Series (Non-Recursive):")

# Call the function
fibonacci_iterative(n)
