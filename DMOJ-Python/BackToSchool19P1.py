# NOT WORKING

num = int(input())
words = []
lengths = []
diffs = []

word = list(map(str, input().split()))

for i in range(len(word)):
    words.append(word[i])
    lengths.append(len(word[i]))

replace_word = str(input())

for i in range(len(words)):
    diffs.append(abs(len(replace_word) - lengths[i]))

lowest = 1001

for i in range(len(diffs)):
    if diffs[i] <= lowest:
        lowest = diffs[i]

pos = []

for i in range(len(diffs)):
    if diffs[i] > lowest:
        diffs[i] = 1001
    elif diffs[i] == lowest:
        pos.append(int(i))

final_lowest = 1001
final_pos = -1

for i in range(len(pos)):
    if pos[i] < final_lowest:
        final_lowest = pos[i]
        final_pos = i

print(pos[i])
