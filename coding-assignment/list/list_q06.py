Problem:- Write a program that generates And returns a list of all even numbers From a
given Range (e.g., From 1 to 100).
solution:-
start = int(input())
end = int(input())
even_numbers = []
for num in range(start, end + 1):
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers from", start, "to", end, "are:", even_numbers)
