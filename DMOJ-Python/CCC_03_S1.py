import sys

input = sys.stdin.readline

current_square = 1

while True:
    move = int(input())
    if current_square + move <= 100:
        if move == 0:
            print("You Quit!")
            sys.exit();
        elif current_square + move == 54:
            current_square = 19
        elif current_square + move == 90:
            current_square = 48
        elif current_square + move == 99:
            current_square = 77
        elif current_square + move == 9:
            current_square = 34
        elif current_square + move == 40:
            current_square = 64
        elif current_square + move == 67:
            current_square = 86
        elif current_square + move == 100:
            print("You are now on square 100")
            print("You Win!")
            sys.exit();
        else:
            current_square += move
    print("You are now on square " + str(current_square))

