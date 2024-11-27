Problem: Take space-separated integers as input and store them in a tuple.

Solution:

user_input = input("Enter space-separated numbers: ")
t = tuple(map(int, user_input.split()))
print("The tuple is:", t)

Example:

Enter space-separated numbers: 10 20 30 40
The tuple is: (10, 20, 30, 40)
