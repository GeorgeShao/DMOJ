import sys

num_cases = int(sys.stdin.readline())

for i in range(num_cases):
    mountainTop = []
    branch = []
    num_carts = int(sys.stdin.readline())
    for j in range(num_carts):
        mountainTop.append(int(sys.stdin.readline()))
    current_num = 1
    noSolution = True
    while(True):
        # if both mountainTop & branches are empty, solution is achieved
        if not mountainTop and not branch:
            noSolution = False
            break
        # if current number is on mountainToop
        if mountainTop and mountainTop[len(mountainTop)-1] == current_num:
            del mountainTop[len(mountainTop)-1]
            current_num += 1
            continue
        # if current number is on branch
        elif branch and branch[len(branch)-1] == current_num:
            del branch[len(branch)-1]
            current_num += 1
            continue
        else:
            if not mountainTop:
                break
            branch.append(mountainTop[len(mountainTop)-1])
            del mountainTop[len(mountainTop)-1]
    if noSolution:
        print("N")
    else:
        print("Y")