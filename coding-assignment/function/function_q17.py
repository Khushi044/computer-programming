Problem: Write a function that returns a list containing the square of each number in the input list.

Solution:
def square_list(lst):
    return [x ** 2 for x in lst]

# Example usage
print(square_list([1, 2, 3]))  # Output: [1, 4, 9]
