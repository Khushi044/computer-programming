Problem:- Write a program that takes a list And an element, And returns the count of occurrences 
of that element In the list.
solution:-
numbers_list = input("Enter a list of numbers (separated by spaces): ").split()
numbers_list = [int(num) for num in numbers_list]
element_to_count = int(input("Enter the element to count: "))
count = 0
for num in numbers_list:
    if num == element_to_count:
        count += 1
print(f"The element {element_to_count} occurs {count} times in the list.")
