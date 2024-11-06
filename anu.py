import random
def partition(arr,low,high):
    pivot= arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i + 1

def Deterministic(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        Deterministic(arr,low,pi - 1)
        Deterministic(arr,pi + 1, high)

def quick_sort_partition(arr,low,high):
    rand_index = random.randint(low,high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition(arr,low,high)

def randomized(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        randomized(arr,low,pi - 1)
        randomized(arr,pi + 1, high)
        
I = int(input("enter number o elements: "))
arr= []
for i in range(I):
    x= int(input(f"enter elements {i+1}"))
    arr.append(x)
    
    
Deterministic(arr,0,I-1)
print(arr)

randomized(arr,0,I-1)
print(arr)
    
    

        

    
    

        