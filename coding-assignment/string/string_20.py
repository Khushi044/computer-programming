Problem: Write a function to check if two strings are anagrams of each other 
(contain the same characters with the same frequencies).
s1 = "listen"
s2 = "silent"
if len(s1) != len(s2):
    print("The strings are not anagrams.")
else:
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    if sorted_s1 == sorted_s2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
