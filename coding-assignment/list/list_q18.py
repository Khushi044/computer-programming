Find the missing number in a list of consecutive numbers
Problem: Given a list of consecutive numbers (with one missing), find the missing number.
Solution:
lst = [1, 2, 3, 5]
n = len(lst) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
missing_number = expected_sum - actual_sum
print(missing_number)  # Output: 4
