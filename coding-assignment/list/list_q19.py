Check if a list is a palindrome
Problem: Check if a given list is a palindrome (i.e., it reads the same forward and backward).

Solution:
lst = [1, 2, 3, 2, 1]
is_palindrome = lst == lst[::-1]
print(is_palindrome)  # Output: True

lst = [1, 2, 3]
is_palindrome = lst == lst[::-1]
print(is_palindrome)  # Output: False
