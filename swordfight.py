
f = open("swordfight.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------
import heapq
class Item:
    def __init__(self, value):
        self.value = value
        self.deleted = False

    def __lt__(self, value):
        return True

    def __repr__(self):
        return "({0}, {1})".format(self.value, self.deleted)

class MaxPQ:
    def __init__(self):
        self.data = []

    def push(self, value):
        item = Item(value)
        heapq.heappush(self.data, (-value, item))

        return item 

    def max(self):
        while self.data[0][1].deleted:
            heapq.heappop(self.data)

        return -self.data[0][0]

import sys

T = int(input())
for i in range(T):
    SWORD_COUNT, MAX_SKILL_DIFF =  [int(x) for x in input().strip().split(" ")]
    CHARLES_SWORDS = [int(x) for x in input().strip().split(" ")]
    DALILA_SWORDS = [int(x) for x in input().strip().split(" ")]

    result = 0

    for win_len in range(1, SWORD_COUNT + 1):
        charles_choices = MaxPQ()
        dalila_choices = MaxPQ()
        charles_items = []
        dalila_items = []
        for pos in range(win_len - 1):
            ci = charles_choices.push(CHARLES_SWORDS[pos]) 
            charles_items.append(ci)

            di = dalila_choices.push(DALILA_SWORDS[pos]) 
            dalila_items.append(di)

        for pos in range(win_len - 1, SWORD_COUNT):
            ci = charles_choices.push(CHARLES_SWORDS[pos]) 
            charles_items.append(ci)

            di = dalila_choices.push(DALILA_SWORDS[pos]) 
            dalila_items.append(di)

            if abs(charles_choices.max() - dalila_choices.max()) <= MAX_SKILL_DIFF:
                result += 1 

            charles_items[pos - win_len + 1].deleted = True
            dalila_items[pos - win_len + 1].deleted = True


    print("Case #{0}: {1} ".format(i + 1, result))
