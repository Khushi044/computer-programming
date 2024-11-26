Problem:- Write a program that checks if two lists are equal (i.e., they have the same elements in the same order).
solution:-
list1_input = input()
list1 = [int(num) for num in list1_input.split()]
list2_input = input()
list2 = [int(num) for num in list2_input.split()]
if list1 == list2:
    print("The lists are equal.")
else:
    print("The lists are not equal.")
