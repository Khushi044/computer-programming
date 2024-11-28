Problem: Write a function that checks if a word exists in a sentence.

Solution:
def word_exists(sentence, word):
    return word in sentence.split()

# Example usage
print(word_exists("hello world", "world"))  # Output: True
