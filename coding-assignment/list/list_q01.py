# Find the Largest and Smallest Element
Problem: Write a Python function that finds the largest and smallest elements in a given list of numbers.
Example:
Input: [3, 1, 4, 1, 5, 9]
Output: Largest: 9, Smallest: 1
SOLUTION:-
list = input().split()
largest = list[0]
smallest = list[0]
for i in list:
    if i >largest:
        largest = i
    elif i < smallest:
        smallest = i
print("largest: ", largest)
print("smallest: ", smallest)
