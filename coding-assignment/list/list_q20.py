Rotate a list by n places
Problem: Rotate a list by n positions to the right.

Solution:
lst = [1, 2, 3, 4, 5]
n = 2
rotated_lst = lst[-n:] + lst[:-n]
print(rotated_lst)  # Output: [4, 5, 1, 2, 3]
