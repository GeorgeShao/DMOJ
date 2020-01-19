import sys

x_coord = 0
y_coord = 0

c = 0
r = 0

c, r = sys.stdin.readline().split()
c = int(c)
r = int(r)

x, y = sys.stdin.readline().split()
x = int(x)
y = int(y)

while (x, y) != (0, 0):

    if 0 <= x_coord + x <= c:
        x_coord += x
    elif x_coord + x < 0:
        x_coord = 0
    elif x_coord + x > 0:
        x_coord = c
    
    if 0 <= y_coord + y <= r:
        y_coord += y
    elif y_coord + y < 0:
        y_coord = 0
    elif y_coord + y > 0:
        y_coord = r
    
    print(x_coord, y_coord)

    x, y = sys.stdin.readline().split()
    x = int(x)
    y = int(y)