topleft = 1
topright = 2
bottomleft = 3
bottomright = 4

newtopleft = 0
newtopright = 0
newbottomleft = 0
newbottomright = 0

moves = str(input())

for i in range(len(moves)):
    if moves[i] == "H":
        newtopleft = bottomleft
        newbottomleft = topleft
        newtopright = bottomright
        newbottomright = topright

    elif moves[i] == "V":
        newtopleft = bottomleft
        newbottomleft = topleft
        newtopright = bottomright
        newbottomright = topright

topleft = newtopleft
topright = newtopright
bottomleft = newbottomleft
bottomright = newbottomright

print(topleft, topright)
print(bottomleft, bottomright)