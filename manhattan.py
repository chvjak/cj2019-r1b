
f = open("manhattan.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------

import sys
T = int(input())
for i in range(T):
    P, MAX_XY =  [int(x) for x in input().strip().split(" ")]

    one_row = [0] * (MAX_XY + 1)
    ew_prefix_sums = [None] * (MAX_XY + 1)
    for j in range(MAX_XY + 1):
        ew_prefix_sums[j] = one_row[:]

    we_prefix_sums = [None] * (MAX_XY + 1)
    for j in range(MAX_XY + 1):
        we_prefix_sums[j] = one_row[:]

    one_row = [0] * (MAX_XY + 1)
    ns_prefix_sums = [None] * (MAX_XY + 1)
    for j in range(MAX_XY + 1):
        ns_prefix_sums[j] = one_row[:]

    sn_prefix_sums = [None] * (MAX_XY + 1)
    for j in range(MAX_XY + 1):
        sn_prefix_sums[j] = one_row[:]


    for person in range(P):
        x, y, heading = input().strip().split(" ")
        x = int(x)
        y = int(y)
        if heading == "W":
            for j in range(0, MAX_XY + 1):
                for k in range(0, x):
                    ew_prefix_sums[j][k] += 1

        if heading == "E":
            for j in range(0, MAX_XY + 1):
                for k in range(x + 1, MAX_XY + 1):
                    we_prefix_sums[j][k] += 1

        if heading == "N":
            for k in range(y + 1, MAX_XY + 1):
                for j in range(0, MAX_XY + 1):
                    sn_prefix_sums[k][j] += 1

        if heading == "S":
            for k in range(0, y):
                for j in range(0, MAX_XY + 1):
                    ns_prefix_sums[k][j] += 1


    max_4way_ps = -sys.maxsize
    max_4way_ps_pos = None 
    
    for j in range(MAX_XY + 1):
        for k in range(MAX_XY + 1):
            if ew_prefix_sums[j][k] + we_prefix_sums[j][k] + sn_prefix_sums[j][k] + ns_prefix_sums[j][k] > max_4way_ps :
                max_4way_ps = ew_prefix_sums[j][k] + we_prefix_sums[j][k] + sn_prefix_sums[j][k] + ns_prefix_sums[j][k] 
                max_4way_ps_pos = (j, k)


    print("Case #{0}: {1} {2}".format(i + 1, max_4way_ps_pos[1], max_4way_ps_pos[0]))
