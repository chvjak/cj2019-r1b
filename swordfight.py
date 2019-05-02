
f = open("swordfight.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------

def is_fair_fight(CHARLES_SWORDS, DALILA_SWORDS, MAX_SKILL_DIFF):
    return  abs(max(CHARLES_SWORDS) - max(DALILA_SWORDS)) <= MAX_SKILL_DIFF


import sys
T = int(input())
for i in range(T):
    SWORD_COUNT, MAX_SKILL_DIFF =  [int(x) for x in input().strip().split(" ")]
    CHARLES_SWORDS = [int(x) for x in input().strip().split(" ")]
    DALILA_SWORDS = [int(x) for x in input().strip().split(" ")]

    result = 0

    for j in range(SWORD_COUNT):
        for k in range(j + 1, SWORD_COUNT + 1):
                result += 1 if is_fair_fight(CHARLES_SWORDS[j:k], DALILA_SWORDS[j:k], MAX_SKILL_DIFF) else 0

    print("Case #{0}: {1} ".format(i + 1, result))
