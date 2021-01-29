alphabet = input()
word = input()

permutations = set()

for i in range(len(word)+1):
    new = word[:i-1] + "" + word[i:]
    permutations.add(new)
    for j in range(len(alphabet)):
        new = word[:i] + alphabet[j] + word[i+1:]
        permutations.add(new)
    for j in range(len(alphabet)):
        new = word[:i] + alphabet[j] + word[i:]
        permutations.add(new)

try:
    permutations.remove(word)
except:
    pass

new_permutations = set()

for each in permutations:
    if len(each) <= len(word)+1:
        new_permutations.add(each)

new_permutations = sorted(new_permutations)

for each in new_permutations:
    print(each)