# NOT FAST ENOUGH

import sys

substrings = []

def printSubSequences(STR, subSTR=""):
    if len(STR) == 0:
        substrings.append(subSTR)
        return
    printSubSequences(STR[:-1], subSTR + STR[-1])
    printSubSequences(STR[:-1], subSTR)
    return

word = input()

printSubSequences(word)

count = 0

for substring in substrings:
    d = {}
    for c in substring:
        if c in d:
            break
        else:
            d[c] = 1
    else:
        count += 1

print(count)