Problem: Write a function that checks if a string is a palindrome.

Solution:
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True
