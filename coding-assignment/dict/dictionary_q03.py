Problem Statement:
Given a list of elements, create a dictionary where the keys are the elements and the values are the count of occurrences.

Solution:
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq_dict = {}

for element in elements:
    freq_dict[element] = freq_dict.get(element, 0) + 1

print(freq_dict)
