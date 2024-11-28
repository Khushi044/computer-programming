Problem: Write a function that counts the number of vowels (a, e, i, o, u) in a given string.

Solution:
def count_vowels(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')
print(count_vowels("hello"))  # Output: 2
