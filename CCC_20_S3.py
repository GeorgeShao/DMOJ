# PARTIALLY WORKING (7/15 PTS)

import sys

a = sys.stdin.readline()[:-1]
b = sys.stdin.readline()[:-1]

permutations = list()

for i in range(len(b)-len(a)+1):
    word1 = a
    word2 = b[i:i+len(a)]
    if b[i:i+len(a)] not in permutations:
        for char in word1:
            if char in word2:
                word1 = word1.replace(char, ' ', 1)
                word2 = word2.replace(char, ' ', 1)
            else:
                break
        if word1.replace(' ', '') == '' and b[i:i+len(a)] not in permutations:
            permutations.append(b[i:i+len(a)])

print(len(permutations))