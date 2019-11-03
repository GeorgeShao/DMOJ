pink_cost = int(input())
green_cost = int(input())
red_cost = int(input())
orange_cost = int(input())
target_total = int(input())

combinations = 0

min_tickets = target_total

for i in range(target_total+1):
    for j in range(target_total+1):
        for k in range(target_total+1):
            for m in range(target_total+1):
                if i*pink_cost + j*green_cost + k*red_cost + m*orange_cost == target_total:
                    print("# of PINK is " + str(i) + " # of GREEN is " + str(j) + " # of RED is " + str(k) + " # of ORANGE is " + str(m))
                    combinations += 1
                    if i + j + k + m < min_tickets:
                        min_tickets = i + j + k + m

print("Total combinations is " + str(combinations) + ".")
print("Minimum number of tickets to print is " + str(min_tickets) + ".")