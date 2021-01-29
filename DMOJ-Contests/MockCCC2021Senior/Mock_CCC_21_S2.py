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
    for char in substring:
        if substring.count(char) > 1:
            break
    else:
        count += 1

print(count)