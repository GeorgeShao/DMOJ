# PARTIALLY WORKING (1/15 PTS)

import sys

my_rows = int(sys.stdin.readline())
nx_cols = int(sys.stdin.readline())

data = list()

def go_backward(x, y):
    global nx_cols, my_rows, data

    found_x = list()
    found_y = list()
    product = (x+1) * (y+1)
    found = False
    for i in range(my_rows):
        temp_row = data[i]
        if str(product) in temp_row:
            for j in range(nx_cols):
                if product == int(temp_row[j]):
                    found_x.append(j)
                    found_y.append(i)
                    found = True
                    if i == 0 and j == 0:
                        print('yes')
                        sys.exit()
    if found == False:
        print("no")
        sys.exit()
    else:
        for i in range(len(found_x)):
            go_backward(found_x[i], found_y[i])
        

for i in range(my_rows):
    input = list(sys.stdin.readline().split(' '))
    data.append(input)
    data[i][nx_cols-1] = data[i][nx_cols-1].replace('\n', '')
    end_x = nx_cols
    end_y = my_rows

go_backward(end_x-1, end_y-1)
