def knapsack_dp(values, weights, capacity):
    n = len(values)
    # Initialize a 2D DP table with 0s
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Input from user
n = int(input("Enter the number of items: "))
values = []
weights = []

for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = int(input("Enter the knapsack capacity: "))

# Solve the knapsack problem
max_value = knapsack_dp(values, weights, capacity)
print(f"The maximum value that can be carried: {max_value}")
