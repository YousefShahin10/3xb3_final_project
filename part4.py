

broken_stations = [2,4,6,7,10,14]

def bsp_solution2(L, m):
    jump_dist = {i:0 for i in range(len(L)-2)}
    for _ in range(m):
        for i in range(len(L)-2):
            jump_dist[i] = L[i+2]-L[i]
        L.pop(min(jump_dist, key=jump_dist.get))
    return L

def bsp_solution3(L, m):
    for _ in range(m):
        min_dist = float('inf')
        min_index = 0
        for i in range(len(L)-2):
            if L[i+2]-L[i] < min_dist:
                min_dist = L[i+2]-L[i]
                min_index = i
        L.pop(min_index+1)
    return L

def bsp_solution(L, m):
    if len(L) <= m+1:
        return L
    return L

def bsp_value(L, m):
    L = bsp_solution(L, m)
    print(L)
    min_dist = float('inf')
    for i in range(len(L)-1):
        min_dist = min(min_dist, L[i+1]-L[i])
    return min_dist

print(bsp_value(broken_stations, 2))



# 2 3 4 6 7 10 14 , 3
# 2 4 6 7 10 14 , 3
# 2 3 4 6  10 14 , 3
# 2  4 6  10 14 , 3
# 2  6  10 14 , 3
# 2 6 10 14