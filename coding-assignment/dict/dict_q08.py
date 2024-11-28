Problem Statement:
Given a dictionary, check if a specific key exists in the dictionary.

Solution:
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists!")
else:
    print(f"Key '{key_to_check}' does not exist.")
Output:
Key 'b' exists!
