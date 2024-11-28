Problem: Write a function that returns the Fibonacci sequence up to n terms.

Solution:
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# Example usage
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
