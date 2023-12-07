from collections import defaultdict, Counter
from typing import List
def rm_node(min_dist, L, m):#returns if its possible ot remove m nodes
    prev_node = L[0]
    removed = 0
    for i in range(1, len(L)):
        if L[i] - prev_node < min_dist:
            removed += 1
            if removed > m:
                # cannot remove more than m nodes
                return False
        else:
            prev_node = L[i]
    return True


def bsp_value(L, m):
    low = 1
    high = L[-1] - L[0]
    while high > low:
        mid = low + (high - low + 1) // 2
        if rm_node(mid, L, m):
            low = mid
        else:
            high = mid-1
    return low


def bsp_solution(L, m):
    if len(L) - m == 2:
        return [L[0]]
    elif len(L) - m < 2:
        return []
    else:
        max_min_dist = bsp_value(L, m)
        prev_node = L[0]
        final_nodes = [prev_node]
        removed_nodes = 0

        for i in range(1, len(L)):
            if L[i] - prev_node < max_min_dist:
                removed_nodes+=1
                if removed_nodes > m:
                    break
            else:
                final_nodes.append(L[i])
                prev_node = L[i]
    return final_nodes

L= [2,4,6,7,10,14]
m = 2

print(bsp_value(L, m))
print(bsp_solution(L, m))

