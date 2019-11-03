orphanages, kids = input().split()
orphanages = int(orphanages)
kids = int(kids)

num_of_bad = [None]*orphanages

for i in range(orphanages):
    num_of_bad[i] = 0
    kid_scores = map(int, input().split())
    for score in kid_scores:
        if score == 1 or score == 10:
            num_of_bad[i] += 1

print(num_of_bad.index(min(num_of_bad)) + 1)
