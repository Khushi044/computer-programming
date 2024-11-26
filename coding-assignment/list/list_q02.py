problem:- write a python program to create a list with elements 1,2,3,4 and 5. display even numbers of the 
list using list comprehension.
solution:-
list1=[1,2,3,4]
print(list1)
list1=[i for i in list1 if i%2==0]
print(list1)
INPUT- [1,2,3,4,5]
OUTPUT - [2,4]
