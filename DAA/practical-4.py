# 4. Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.

# 1. DP solution
# Function to solve 0-1 Knapsack problem using Dynamic Programming
def knapsack_dp(weights, values, capacity):
    n = len(values)
    # Create a DP table with size (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Either include the item or exclude it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    # Return the maximum value for the given capacity
    return dp[n][capacity]
# Driver code
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_value = knapsack_dp(weights, values, capacity)
    print(f"Maximum value in knapsack = {max_value}")

# 2. Branch and bound strategy
from queue import PriorityQueue
# Node structure for Branch and Bound

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    # For priority queue (max heap) comparison
    def __lt__(self, other):
        return self.bound > other.bound

# Function to calculate upper bound
def calculate_bound(node, n, capacity, values, weights):
    if node.weight >= capacity:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight
    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        profit_bound += values[j]
        j += 1
    if j < n:
        profit_bound += (capacity - total_weight) * (values[j] / weights[j])
    return profit_bound

# Function to solve 0-1 Knapsack problem using Branch and Bound
def knapsack_bb(values, weights, capacity):
    n = len(values)
    q = PriorityQueue()
    # Sort items by value-to-weight ratio
    items = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    sorted_weights = [weights[i] for i in items]
    sorted_values = [values[i] for i in items]
    # Create a dummy node and insert it into the queue
    u = Node(-1, 0, 0, 0)
    v = Node(0, 0, 0, 0)
    u.bound = calculate_bound(u, n, capacity, sorted_values, sorted_weights)
    q.put(u)
    max_profit = 0
    while not q.empty():
        u = q.get()  # Get the node with the highest bound
        if u.bound > max_profit:
            # Branching: Exclude or include the next item
            v.level = u.level + 1
            v.weight = u.weight + sorted_weights[v.level]
            v.profit = u.profit + sorted_values[v.level]
            # Check if including the item is feasible
            if v.weight <= capacity and v.profit > max_profit:
                max_profit = v.profit
            # Calculate bound for including the item
            v.bound = calculate_bound(v, n, capacity, sorted_values, sorted_weights)
            if v.bound > max_profit:
                q.put(v)
            # Do the same for excluding the item
            v.weight = u.weight
            v.profit = u.profit
            v.bound = calculate_bound(v, n, capacity, sorted_values, sorted_weights)
            if v.bound > max_profit:
                q.put(v)
    return max_profit

# Driver code
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_value = knapsack_bb(values, weights, capacity)
    print(f"Maximum value in knapsack = {max_value}")