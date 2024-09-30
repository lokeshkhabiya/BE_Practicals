# Mini Project - Write a program to implement matrix multiplication. 
# Also implement multithreaded matrix multiplication with either one thread per row or one thread per cell. 
# Analyze and compare their performance

# 1. Regular matrix multiplication 
import time

def matrix_multiply(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    # Initialize result matrix
    C = [[0 for _ in range(p)] for _ in range(n)]
    # Perform matrix multiplication
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Main execution
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
start = time.time()
C = matrix_multiply(A, B)
end = time.time()
print("Resulting Matrix C (Single-threaded):")
for row in C:
    print(row)
print(f"Time taken (Single-threaded): {end - start} seconds")

# ------------------------------------------------------------------------------------------------ #

# 2. MultiThreded matrix multiplication 
import time
import threading

# Thread function to compute one row
def multiply_row(A, B, C, row):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    for j in range(p):
        C[row][j] = sum(A[row][k] * B[k][j] for k in range(m))

def matrix_multiply_multithreaded(A, B):
    n = len(A)
    p = len(B[0])
    # Initialize result matrix
    C = [[0 for _ in range(p)] for _ in range(n)]
    # Create threads, one per row
    threads = []
    for i in range(n):
        thread = threading.Thread(target=multiply_row, args=(A, B, C, i))
        threads.append(thread)
        thread.start()
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    return C

# Main execution
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
start = time.time()
C = matrix_multiply_multithreaded(A, B)
end = time.time()
print("Resulting Matrix C (Multithreaded - One Thread per Row):")
for row in C:
    print(row)
print(f"Time taken (Multithreaded - One Thread per Row): {end - start} seconds")

