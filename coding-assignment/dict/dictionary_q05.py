Problem Statement:
Given a dictionary, remove all key-value pairs where the value is None.

Solution:
dict_with_none = {'a': 1, 'b': None, 'c': 3, 'd': None}
cleaned_dict = {key: value for key, value in dict_with_none.items() if value is not None}
print(cleaned_dict)
