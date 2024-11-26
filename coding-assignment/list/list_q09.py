Problem:-Write a program that removes all occurrences of a specific element from a list.
solution:-
numbers_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers_input.split()]
element_to_remove = int(input("Enter the element to remove: "))
while element_to_remove in numbers_list:
    numbers_list.remove(element_to_remove)
print("The list after removing the element is:", numbers_list)
