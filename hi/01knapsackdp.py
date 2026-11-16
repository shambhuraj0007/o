
# Function to solve 0-1 Knapsack using Dynamic Programming
def knapsack(weights, profits, capacity):

    # Find the total number of items
    n = len(weights)

    # Create a DP table with n+1 rows and capacity+1 columns
    dp = [[0 for x in range(capacity + 1)]
          for y in range(n + 1)]

    # Traverse each item
    for i in range(1, n + 1):

        # Traverse every possible capacity
        for w in range(1, capacity + 1):

            # Check if current item's weight is within capacity
            if weights[i - 1] <= w:

                # Calculate profit if item is included
                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]

                # Calculate profit if item is excluded
                exclude = dp[i - 1][w]

                # Store the maximum of both choices
                dp[i][w] = max(include, exclude)

            else:

                # Exclude the item if its weight is too large
                dp[i][w] = dp[i - 1][w]

    # Return the maximum profit from the DP table
    return dp[n][capacity]


# Accept the number of items from the user
n = int(input("Enter number of items: "))

# Create an empty list to store weights
weights = []

# Create an empty list to store profits
profits = []

# Accept weight and profit of each item
for i in range(n):

    # Read the weight of the current item
    w = int(input("Enter weight of item " + str(i + 1) + ": "))

    # Read the profit of the current item
    p = int(input("Enter profit of item " + str(i + 1) + ": "))

    # Check that weight is positive
    if w <= 0:
        raise ValueError("Weight must be positive.")

    # Store the weight in the list
    weights.append(w)

    # Store the profit in the list
    profits.append(p)

# Accept the maximum knapsack capacity
capacity = int(input("Enter knapsack capacity: "))

# Check that capacity is non-negative
if capacity < 0:
    raise ValueError("Capacity cannot be negative.")

# Call the knapsack function
max_profit = knapsack(weights, profits, capacity)

# Display the maximum profit
print("Maximum Profit =", max_profit)












