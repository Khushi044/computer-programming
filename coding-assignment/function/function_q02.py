Problem: Write a function that checks if a number is even or odd.

Solution:
def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even_or_odd(7))  # Output: Odd
