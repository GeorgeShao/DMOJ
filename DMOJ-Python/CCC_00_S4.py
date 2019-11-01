# Not Working

import sys

dist = int(input())
num_dist = int(input())
dists = [None] * num_dist

for i in range(num_dist):
    dists[i] = int(input())

dists.sort()

strokes = 1

def return_left(left):
    global strokes, dists
    flag = None
    for distance in dists:
        if min(dists) > left:
            print("Roberta acknowledges defeat.")
            sys.exit(0)
        if distance == left:  
            return distance
        if distance < left:
            flag = distance
    temp_distance = round(left - flag)
    strokes += 1
    return [flag] + [return_left(temp_distance)]

return_left(dist)
print(f"Roberta wins in {strokes} strokes.")