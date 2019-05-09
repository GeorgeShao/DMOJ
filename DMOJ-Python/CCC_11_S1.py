sentences = int(input())

english = 0
french = 0

for i in range(sentences):
    text = input()
    for char in text:
        if char == "t" or char == "T":
            english += 1
        elif char == "s" or char == "S":
            french += 1

if english > french:
    print("English")
elif french > english:
    print("French")
else:
    print("French")