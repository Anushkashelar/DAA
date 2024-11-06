def fractional_knapsack(value, weight, capacity):
    # Calculate value/weight ratio for each item and sort by this ratio in descending order
    items = sorted(zip(value, weight), key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0
    for v, w in items:
        if capacity >= w:
            total_value += v  # Take the whole item
            capacity -= w
        else:
            total_value += v * (capacity / w)  # Take the fraction that fits
            break

    return total_value

# Input from user
n = int(input("Enter the number of items: "))
value = []
weight = []

for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    value.append(v)
    weight.append(w)

capacity = float(input("Enter the knapsack capacity: "))

# Calculate the maximum value
max_value = fractional_knapsack(value, weight, capacity)
print(f"The maximum value of items that can be carried: {max_value}")
