Problem: Write a function that removes duplicate characters from a string.

Solution:
def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

# Example usage
print(remove_duplicates("aabbcc"))  # Output: "ab
