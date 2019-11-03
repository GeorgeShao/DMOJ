# PARTIALLY WORKING

import sys

computers = int(input())

best_score = 0
second_best_score = 0

best_computer = ""
second_best_computer = ""

for i in range(computers):
    name, r, s, d = sys.stdin.readline().split()
    r = int(r)
    s = int(s)
    d = int(d)

    score = 2*r + 3*s + d

    if score > best_score:
        second_best_score = best_score
        best_score = score
        second_best_computer = best_computer
        best_computer = name
    elif score > second_best_score:
        second_best_score = score
        second_best_computer = name
    elif score == best_score and score == second_best_score:
        if name < best_computer:
            second_best_score = best_score
            best_score = score
            second_best_computer = best_computer
            best_computer = name
        elif name < second_best_computer:
            second_best_score = score
            second_best_computer = name
    elif score == best_score:
        if score > second_best_score:
            if name < best_computer:
                second_best_score = best_score
                best_score = score
                second_best_computer = best_computer
                best_computer = name
    elif score == second_best_score:
        if name < second_best_computer:
            second_best_score = score
            second_best_computer = name

print(best_computer)
print(second_best_computer)