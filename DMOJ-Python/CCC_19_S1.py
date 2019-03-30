import sys

input = sys.stdin.readline

topleft = 1
topright = 2
bottomleft = 3
bottomright = 4

newtopleft = 0
newtopright = 0
newbottomleft = 0
newbottomright = 0

moves = input()

for i in range(len(moves)):
    # flip over x axis
    if moves[i] == "H":
        newtopleft = bottomleft
        newbottomleft = topleft
        newtopright = bottomright
        newbottomright = topright
    # flip over y axis
    elif moves[i] == "V":
        newtopleft = topright
        newbottomleft = bottomright
        newtopright = topleft
        newbottomright = bottomleft

    topleft = newtopleft
    topright = newtopright
    bottomleft = newbottomleft
    bottomright = newbottomright

print(topleft, topright)
print(bottomleft, bottomright)