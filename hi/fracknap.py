
# Function to solve Fractional Knapsack
def fractional_knapsack(weights, profits, capacity):

    # Find the total number of items
    n = len(weights)

    # Calculate profit-to-weight ratio for each item
    ratio = [profits[i] / weights[i] for i in range(n)]

    # Sort item indexes by ratio in descending order
    items = sorted(range(n), key=lambda i: ratio[i], reverse=True)

    # Initialize total profit as zero
    total_profit = 0

    # Traverse items according to highest ratio
    for i in items:

        # Check whether the complete item fits
        if weights[i] <= capacity:

            # Take the complete item
            total_profit += profits[i]

            # Reduce the remaining capacity
            capacity -= weights[i]

        # If the complete item does not fit
        else:

            # Take only the required fraction
            fraction = capacity / weights[i]

            # Add fractional profit
            total_profit += profits[i] * fraction

            # Knapsack is now full
            capacity = 0

            # Stop the loop
            break

    # Return the maximum profit
    return total_profit


# Accept the number of items
n = int(input("Enter number of items: "))

# Create an empty list for weights
weights = []

# Create an empty list for profits
profits = []

# Accept weight and profit of each item
for i in range(n):

    # Read the weight of the item
    w = float(input("Enter weight of item " + str(i + 1) + ": "))

    # Read the profit of the item
    p = float(input("Enter profit of item " + str(i + 1) + ": "))

    # Check that weight is positive
    if w <= 0:
        raise ValueError("Weight must be positive.")

    # Store the weight
    weights.append(w)

    # Store the profit
    profits.append(p)

# Accept knapsack capacity
capacity = float(input("Enter knapsack capacity: "))

# Check that capacity is non-negative
if capacity < 0:
    raise ValueError("Capacity cannot be negative.")

# Call the Fractional Knapsack function
max_profit = fractional_knapsack(weights, profits, capacity)

# Display the maximum profit
print("Maximum Profit =", max_profit)
