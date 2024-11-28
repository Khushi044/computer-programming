Find common elements in two lists
Question: Find common elements between [1, 2, 3] and [2, 3, 4].
Solution:
lst1 = [1, 2, 3]
lst2 = [2, 3, 4]
common_elements = list(set(lst1) & set(lst2))
print(common_elements)  # Output: [2, 3] 
