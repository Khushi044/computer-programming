# THE SHORTEST WORD FINDER
a = input()
word = a.split()
b = min(word,key=len)
print(b)
INPUT - This is a ball
OUTPUT - a
