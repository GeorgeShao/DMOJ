import sys

word1 = sys.stdin.readline()
word2 = sys.stdin.readline()

for char in word1:
    if char in word2:
        word2 = word2.replace(char, '', 1)

for char in word2:
    if char != '*':
        print("N")
        sys.exit()

print("A")