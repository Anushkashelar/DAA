def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot correctly
    return i + 1

def QS(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        QS(arr, low, pi - 1)  # Recursively sort left part
        QS(arr, pi + 1, high)  # Recursively sort right part

I = int(input("Enter the number of elements: "))
arr = []
for i in range(I):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

QS(arr, 0, I - 1)  # Sorting the entire array
print("Sorted array:", arr)
        