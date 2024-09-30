# Write a program for analysis of quick sort by using deterministic and randomized variant.

# 1. Deterministic quick sort
import time
# Function to partition the array
def partition(arr, low, high):
    pivot = arr[high]  # Last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Deterministic QuickSort function
def quicksort_deterministic(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_deterministic(arr, low, pi - 1)
        quicksort_deterministic(arr, pi + 1, high)

# Main execution
arr = [10, 80, 30, 90, 40, 50, 70]
start = time.time()
quicksort_deterministic(arr, 0, len(arr) - 1)

end = time.time()
print(f"Sorted array: {arr}")
print(f"Deterministic QuickSort Time: {end - start} seconds")

# ------------------------------------------------------------------ #

# 2. Randomized variant
import time
import random

# Function to partition the array with random pivot
def randomized_partition(arr, low, high):
    random_pivot = random.randint(low, high)
    arr[random_pivot], arr[high] = arr[high], arr[random_pivot] # Swap random pivot with last element
    return partition(arr, low, high)

# Randomized QuickSort function
def quicksort_randomized(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        quicksort_randomized(arr, low, pi - 1)
        quicksort_randomized(arr, pi + 1, high)

# Main execution
arr = [10, 80, 30, 90, 40, 50, 70]
start = time.time()
quicksort_randomized(arr, 0, len(arr) - 1)
end = time.time()
print(f"Sorted array: {arr}")
print(f"Randomized QuickSort Time: {end - start} seconds")