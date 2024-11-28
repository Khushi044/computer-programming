Find the second largest element in a list
Problem: Find the second largest element in a given list of numbers.

Solution:
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

# Example usage
lst = [12, 35, 1, 10, 34, 1]
print(second_largest(lst))  # Output: 34
