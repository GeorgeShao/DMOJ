import sys

num_heights = int(sys.stdin.readline().replace('\n', ''))

heights = []

heights = sys.stdin.readline().replace('\n', '').split()

for i in range(len(heights)):
    heights[i] = int(heights[i])

widths = []

widths = sys.stdin.readline().replace('\n', '').split()

for i in range(len(widths)):
    widths[i] = int(widths[i])

total_area = 0

for i in range(len(widths)):
    area = widths[i] * ((heights[i] + heights[i+1])/2)
    total_area += area

print(total_area)