Problem Statement:
Given a dictionary, find the key that has the maximum value.

Solution:
my_dict = {'a': 10, 'b': 20, 'c': 5}
max_key = max(my_dict, key=my_dict.get)
print(max_key)
Output:
'b'
