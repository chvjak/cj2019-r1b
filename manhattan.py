
f = open("manhattan.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------

import sys

def is_intersecting(rect1, rect2):
    (x1, y1), (x2, y2) = get_intersection(rect1, rect2)
    return x1 <= x2 and y1 <= y2 

def get_intersection(rect1, rect2):
    return ((max(rect1[0][0], rect2[0][0]), max(rect1[0][1], rect2[0][1])), (min(rect1[1][0], rect2[1][0]), min(rect1[1][1], rect2[1][1])))

from functools import reduce
def get_intersections_rect(rectangles_by_lx, rectangles_by_rx, global_max_intersections_key_pair):
    active_rectangles = []
    for i in range(global_max_intersections_key_pair[0] + 1):
        if len(rectangles_by_lx[i]) > 0:
            active_rectangles += rectangles_by_lx[i]

        if i == global_max_intersections_key_pair[0]:
            keys = set()
            segments_l = defaultdict(list)
            segments_r = defaultdict(list)

            for rect in active_rectangles:
                l_key, r_key = rect[0][1], rect[1][1]
                segments_l[l_key].append(rect)
                segments_r[r_key].append(rect)
                keys |= set([l_key, r_key])

            keys_list = list(keys)
            keys_list.sort()

            active_segments = []
            for key in keys_list:
                if len(segments_l[key]):
                    active_segments += segments_l[key]

                if key == global_max_intersections_key_pair[1]:
                    res = reduce(get_intersection, active_segments)
                    return res

                for segment in segments_r[i]:
                    active_segments.remove(segment)

        for rect in rectangles_by_rx[i]:
            active_rectangles.remove(rect)


# 2D scanline!
from collections import defaultdict
def count_intersections(active_rectangles):
    segments_l = defaultdict(list)
    segments_r = defaultdict(list)

    keys = set()
    for rect in active_rectangles:
       l_key, r_key = rect[0][1], rect[1][1]
       segments_l[l_key].append(rect)
       segments_r[r_key].append(rect)
       keys |= set([l_key, r_key])

    keys_list = list(keys)
    keys_list.sort()

    active_segments = []
    max_intersections = 0
    max_intersection_key = -1
    for key in keys_list:
        if len(segments_l[key]):
            active_segments += segments_l[key]

            if max_intersections < len(active_segments):
                max_intersections = len(active_segments)
                max_intersection_key = key

        for segment in segments_r[key]:
            active_segments.remove(segment)

    return  max_intersections, max_intersection_key 


def maximum_overlap_rectangle(rectangles_by_lx, rectangles_by_rx):
    MAX_XY = len(rectangles_by_lx)

    active_rectangles = []
    global_max_intersections = 0
    global_max_intersections_rect = ()
    for i in range(MAX_XY):
        if len(rectangles_by_lx[i]) > 0:
            active_rectangles += rectangles_by_lx[i]
            max_intersections, max_intersections_key = count_intersections(active_rectangles)

            if max_intersections > global_max_intersections:
                global_max_intersections = max_intersections 
                global_max_intersections_key_pair = (i, max_intersections_key)

        for rect in rectangles_by_rx[i]:
            active_rectangles.remove(rect)

    return get_intersections_rect(rectangles_by_lx, rectangles_by_rx, global_max_intersections_key_pair) 


def create_rect(x, y, heading):
        if heading == "W":
            # bottom left, upper right
            return ((0, 0), (x - 1, MAX_XY))

        if heading == "E":
            # bottom left, upper right
            return ((x + 1, 0), (MAX_XY, MAX_XY))

        if heading == "N":
            # bottom left, upper right
            return ((0, y + 1), (MAX_XY, MAX_XY))

        if heading == "S":
            # bottom left, upper right
            return ((0, 0), (MAX_XY, y - 1))


T = int(input())
for i in range(T):
    P, MAX_XY =  [int(x) for x in input().strip().split(" ")]

    rectangles_by_lx = [None] * (MAX_XY + 1)
    rectangles_by_rx = [None] * (MAX_XY + 1)

    for j in range(MAX_XY + 1):
        rectangles_by_lx[j] = []
        rectangles_by_rx[j] = []

    for person in range(P):
        x, y, heading = input().strip().split(" ")
        x = int(x)
        y = int(y)

        rectangle = create_rect(x, y, heading)
        rectangles_by_lx[rectangle[0][0]].append(rectangle)
        rectangles_by_rx[rectangle[1][0]].append(rectangle)

    res_rect = maximum_overlap_rectangle(rectangles_by_lx, rectangles_by_rx)         

    print("Case #{0}: {1} {2}".format(i + 1, res_rect[0][0], res_rect[0][1]))
