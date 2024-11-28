Problem: Write a function that removes all spaces from a string.
s = "Hello World! How are you?"
result = ""
for char in s:
    if char != " ":
        result += char
print("String without spaces:", result)
