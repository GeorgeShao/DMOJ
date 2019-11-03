# NOT WORKING

import sys

grid_size = int(sys.stdin.readline())
sunflowers = [[0 for i in range(grid_size)] for i in range(grid_size)]

for i in range(grid_size):
    temp_input = sys.stdin.readline()
    for j in range(grid_size):
        sunflowers[i][j] = temp_input.split()[j]

if sunflowers[0][0] < sunflowers[0][-1] and sunflowers[0][0] < sunflowers[-1][0] and sunflowers[-1][0] < sunflowers[-1][-1] and sunflowers[0][-1] < sunflowers[-1][-1]:
    for i in range(grid_size):
        print(" ".join(list(map(str, sunflowers[i]))))

elif sunflowers[0][-1] < sunflowers[-1][-1] and sunflowers[0][-1] < sunflowers[0][0] and sunflowers[0][0] < sunflowers[-1][0] and sunflowers[-1][-1] < sunflowers[-1][0]:
    rotated_sunflowers = list(zip(*sunflowers[::-1]))
    rotated_sunflowers = list(zip(*rotated_sunflowers[::-1]))
    rotated_sunflowers = list(zip(*rotated_sunflowers[::-1]))
    for i in range(grid_size):
        print(" ".join(list(map(str, rotated_sunflowers[i]))))

elif sunflowers[-1][0] < sunflowers[0][0] and sunflowers[-1][0] < sunflowers[-1][-1] and sunflowers[-1][-1] < sunflowers[0][-1] and sunflowers[0][0] < sunflowers[0][-1]:
    rotated_sunflowers = list(zip(*sunflowers[::-1]))
    for i in range(grid_size):
        print(" ".join(list(map(str, rotated_sunflowers[i]))))
    
elif sunflowers[-1][-1] < sunflowers[-1][0] and sunflowers[-1][-1] < sunflowers[0][-1] and sunflowers[0][-1] < sunflowers[0][0] and sunflowers[-1][0] < sunflowers[0][0]:
    rotated_sunflowers = list(zip(*sunflowers[::-1]))
    rotated_sunflowers = list(zip(*rotated_sunflowers[::-1]))
    for i in range(grid_size):
        print(" ".join(list(map(str, rotated_sunflowers[i]))))
    
