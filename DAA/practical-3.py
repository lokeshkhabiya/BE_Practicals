# 3. Write a program to solve a fractional Knapsack problem using a greedy method.

# Class to represent an item with value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate the maximum value that can be carried
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.value / item.weight, reverse=True)
    total_value = 0.0  # To store the total value
    for item in items:
        if capacity >= item.weight:
            # If the item can fit in the remaining capacity, take it all
            capacity -= item.weight
            total_value += item.value
        else:
            # Otherwise, take the fraction of the item that fits
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break  # The knapsack is full
    return total_value

# Driver code
if __name__ == "__main__":
    # List of items (value, weight)
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    # Capacity of the knapsack
    capacity = 50
    # Calculate and print the maximum value
    max_value = fractional_knapsack(items, capacity)
    print(f"Maximum value we can obtain = {max_value}")
