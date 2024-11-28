Find the most frequent element in a list
Problem: Find the element that appears most frequently in the list.

Solution:
from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

# Example usage
lst = [1, 2, 3, 2, 4, 2, 5]
print(most_frequent(lst))  # Output: 2
