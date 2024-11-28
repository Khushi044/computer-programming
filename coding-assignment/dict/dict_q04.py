Problem Statement:
Given a dictionary where the values are unique, create a new dictionary where the
keys are the values from the original dictionary, and the values are the keys.

Solution:
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)
