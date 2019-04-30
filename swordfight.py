
f = open("swordfight.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------

def fair_fight_count(CHARLES_SWORDS, DALILA_SWORDS, MAX_SKILL_DIFF):
    matching_swords  = set()
    for c in CHARLES_SWORDS:
        for d in DALILA_SWORDS:
            if abs(c - d) <= MAX_SKILL_DIFF:
                matching_swords.add((c,d))

    print(matching_swords)
    return len(matching_swords)


import sys
T = int(input())
for i in range(T):
    SWORD_COUNT, MAX_SKILL_DIFF =  [int(x) for x in input().strip().split(" ")]
    CHARLES_SWORDS = [int(x) for x in input().strip().split(" ")]
    DALILA_SWORDS = [int(x) for x in input().strip().split(" ")]

    result = 0

    for j in range(SWORD_COUNT):
        for k in range(j + 1, SWORD_COUNT + 1):
                result += fair_fight_count(CHARLES_SWORDS[j:k], DALILA_SWORDS[j:k], MAX_SKILL_DIFF)
        
    print("Case #{0}: {1} ".format(i + 1, result))
