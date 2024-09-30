# Write a program non-recursive and recursive program to calculate Fibonacci numbers and
# analyze their time and space complexity.


# 1. Non Recursive
def fibonacci_non_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        fib = a + b
        a = b
        b = fib
    return b

print("Fibonacci for first 10 numbers is ( non recursive ): ", fibonacci_non_recursive(10))

def fibonacci_recursive(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);

print("Fibonacci for first 10 numbers is ( recursive ):", fibonacci_recursive(10))