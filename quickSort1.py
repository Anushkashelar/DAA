import random

# Deterministic partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot correctly
    return i + 1

# Deterministic Quick Sort
def quick_sort_deterministic(arr, low, high):  
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_deterministic(arr, low, pi - 1)  # Recursively sort left part
        quick_sort_deterministic(arr, pi + 1, high)  # Recursively sort right part

# Randomized partition function
def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)  # Choose a random pivot
    arr[high], arr[rand_index] = arr[rand_index], arr[high]  # Swap pivot with the last element
    return partition(arr, low, high)  # Use the same partition logic

# Randomized Quick Sort
def quick_sort_randomized(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        quick_sort_randomized(arr, low, pi - 1)  # Recursively sort left part
        quick_sort_randomized(arr, pi + 1, high)  # Recursively sort right part

# Input and driver code
I = int(input("Enter the number of elements: "))
arr = []
for i in range(I):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

# Sorting using Deterministic Quick Sort
print("Original array:", arr)
quick_sort_deterministic(arr, 0, I - 1)
print("Sorted array (Deterministic):", arr)

# # Reset the array to original input
arr = []
for i in range(I):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

# Sorting using Randomized Quick Sort
print("Original array:", arr)
quick_sort_randomized(arr, 0, I - 1)
print("Sorted array (Randomized):", arr)
