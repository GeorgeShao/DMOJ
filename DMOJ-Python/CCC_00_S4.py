import sys

distance = int(sys.stdin.readline())
num_strokes = int(sys.stdin.readline())

stroke_dists = []
stroke_costs = [0] + [False] * (distance)

for i in range(num_strokes):
    stroke_dists.append(int(sys.stdin.readline()))

for i in range(1, distance+1):
    new_costs = []
    for j in stroke_dists:
        if j <= i:
            if stroke_costs[i-j] is not False:
                new_costs.append(stroke_costs[i-j] + 1)
    if new_costs:
        stroke_costs[i] = min(new_costs)
    else:
        stroke_costs[i] = False

if stroke_costs[distance]:
    print(f"Roberta wins in {stroke_costs[distance]} strokes.")
else:
    print("Roberta acknowledges defeat.")