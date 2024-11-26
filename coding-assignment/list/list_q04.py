problem:-Write a program to Return prime numbers From a list.
solution:-
numbers_list = [10, 23, 4, 7, 15, 31, 50, 13]
prime_numbers = []
for num in numbers_list:
    if num > 1: 
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
print("Prime numbers in the list:", prime_numbers)
