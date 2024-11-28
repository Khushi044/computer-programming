Problem Statement:
Given two dictionaries dict1 and dict2, merge them into one dictionary. 
If both dictionaries have the same key, the value from dict2 should overwrite the value from dict1.

Solution:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)  # Merges dict2 into dict1
print(dict1)
