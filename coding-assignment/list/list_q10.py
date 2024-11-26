Problem:-Write a program that rotates a list to the right by a specified number of positions. easy and without function
solution:-
numbers_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers_input.split()]
positions = int(input("Enter the number of positions to rotate the list: "))
positions = positions % len(numbers_list)
rotated_list = numbers_list[-positions:] + numbers_list[:-positions]
print("The rotated list is:", rotated_list)
