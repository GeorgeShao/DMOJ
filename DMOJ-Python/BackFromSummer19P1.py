orphanages, kids = map(int, input().split())

num_of_bad = []

for i in range(orphanages):
    kid_scores = list(map(int, input().split()))
    print(kid_scores)
    for score in kid_scores:
        if score == 1 or score == 10:
            num_of_bad[i] += 1

print(num_of_bad.index(min(num_of_bad)))
