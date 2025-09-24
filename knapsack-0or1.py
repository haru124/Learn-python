def knapsack_with_items(weights, values, capacity):
    n = len(weights)
    
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find which items were included
    w = capacity
    included_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i-1)  # store index of included item
            w -= weights[i - 1]
    
    included_items.reverse()  # optional: original order
    
    # Print included items details
    print("Items included in the knapsack:")
    for idx in included_items:
        print(f"Item {idx}: Weight = {weights[idx]}, Value = {values[idx]}")
    
    return dp[n][capacity]

# Example usage
weights = [2, 4, 6, 9]
values = [10, 10, 12, 18]
capacity = 15

max_value = knapsack_with_items(weights, values, capacity)
print(f"Maximum value: {max_value}")
