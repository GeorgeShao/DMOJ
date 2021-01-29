# NOT WORKING (WORKING BUT TOO SLOW)

import sys

substrings = []

def printSubSequences(STR, subSTR=""):
    if len(STR) == 0:
        substrings.append(subSTR)
        return
    printSubSequences(STR[:-1], subSTR + STR[-1])
    printSubSequences(STR[:-1], subSTR)
    return

word = str(sys.stdin.readline().replace("/n", "").strip())

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