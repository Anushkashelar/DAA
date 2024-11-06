# Non-recursive (Iterative) Fibonacci
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib_0 = 0
    fib_1 = 1
    
    for i in range(2, n+1):
        fib_next = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib_next
    
    return fib_1

# Driver code
n = int(input("Enter the value of n for Fibonacci: "))
print(f"Fibonacci number (Iterative) for {n}: {fibonacci_iterative(n)}")



# Recursive Fibonacci
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Driver code
n = int(input("Enter the value of n for Fibonacci: "))
print(f"Fibonacci number (Recursive) for {n}: {fibonacci_recursive(n)}")
