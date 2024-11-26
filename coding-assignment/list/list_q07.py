Problem:-Write a program that multiplies all the elements in a list and returns the product.
solution:
numbers_input = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers_input.split()]
product = 1
for num in numbers_list:
    product *= num
print("The product of all elements in the list is:", product)
