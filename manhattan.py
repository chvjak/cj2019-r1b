
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

def count_intersections(active_rectangles):
    bit_len = len(active_rectangles)
    max_rect_count = 0

    # 2^N :(
    for i in range(2 ** bit_len):       
        intersection = None
        rect_count = 1
        for j in range(0, bit_len):
            if 2 ** j & i == 2 ** j:
                if intersection is not None and is_intersecting(intersection ,  active_rectangles[j]):
                    intersection = get_intersection(intersection, active_rectangles[j])
                    rect_count += 1
                elif 2 ** j & i == 2 ** j and intersection is None:
                    intersection = active_rectangles[j]
                else:
                    break

        if rect_count > max_rect_count :
            max_rect_count = rect_count 
            max_intersection = intersection if intersection is not None else active_rectangles[0]

    return  max_rect_count, max_intersection

def maximum_overlap_rectangle(rectangles_by_lx, rectangles_by_rx):
    MAX_XY = len(rectangles_by_lx)

    active_rectangles = []
    global_max_intersections = 0
    global_max_intersections_rect = ()
    for i in range(MAX_XY):
        if len(rectangles_by_lx[i]) > 0:
            active_rectangles += rectangles_by_lx[i]
            max_intersections, max_intersections_rect = count_intersections(active_rectangles)

            if max_intersections > global_max_intersections:
                global_max_intersections = max_intersections 
                global_max_intersections_rect = max_intersections_rect

        for rect in rectangles_by_rx[i]:
            active_rectangles.remove(rect)


    return global_max_intersections_rect 


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
