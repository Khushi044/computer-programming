problem:- create a list .pass the list to a function and print the contents of the list inside the function.
solution:-
def print_list(lst):
  for num in lst:
    print(num,end=" ")
lst= list(input())
print_list(lst)
