Problem: Write a function that returns the first non-repeating character in a string.
s = "swiss"
for i in range(len(s)):
    if s.count(s[i]) == 1:
        print("First non-repeating character:", s[i])
        break
else:
    print("No non-repeating character found.")
