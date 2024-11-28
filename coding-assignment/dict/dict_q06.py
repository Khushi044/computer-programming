Problem Statement:
Given a dictionary, sort it by its values in ascending order.

Solution:
unsorted_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
Output:
{'b': 1, 'c': 2, 'a': 3}
