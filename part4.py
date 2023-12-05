

def find_smallest_indices(input_list):
    if not input_list:
        return "Input list is empty"
    # Find the minimum value in the list
    min_value = min(input_list)
    # Find the indices of the minimum value using a list comprehension
    indices = [index for index, value in enumerate(input_list) if value == min_value]
    return indices

def calculate_distances(L, distances):
    length = len(L)
    for i in range(length-1):
        distances[i] = (L[i+1] - L[i])
        
def bsp_solution(L,m):
    distances=[]
    print(len(L))
    length = len(L)
    for i in range(length-1):
        distances.append(0)
    calculate_distances(L, distances)
    for i in range(m):
        print('distances in the works: ', distances)
        for j in find_smallest_indices(distances):
            print(j)
            if j == 0:
                print(distances)
                print('activated')
            elif len(distances) == 2:
                L.remove(L[1])
            else:
                lowest_val_index = j
                first_length = distances[lowest_val_index-1]
                second_length = distances[lowest_val_index+1]
                if len(find_smallest_indices(distances)) == 1:
                    if first_length > second_length:
                        print('first if')
                        print("number removed is ", L[lowest_val_index])
                        L.remove(L[lowest_val_index])
                    elif first_length < second_length:
                        print('second if')
                        print("number removed is ", L[lowest_val_index +1])
                        L.remove(L[lowest_val_index + 1])
                    else:
                        print('third if')
                        print("number removed is ", L[lowest_val_index])
                        L.remove(L[lowest_val_index])
                else:
                    L.remove(L[lowest_val_index])
                distances.remove(distances[j])
                calculate_distances(L, distances)
                print("in the works list: ", L)
                break
    return L

def bsp_value(L, m):
    L = bsp_solution(L, m)
    print(L)
    min_dist = float('inf')
    for i in range(len(L)-1):
        min_dist = min(min_dist, L[i+1]-L[i])
    return min_dist

# print(bsp_value(broken_stations, 2))

L=[2,4,6,7,10,14]
l = [5,2,8,2,9,1]
# print(find_smallest_indices(l))
# print(find_smallest_value(L))
L = [2, 3, 4, 6, 7, 10, 14]
print(bsp_solution(L, 3))

# 2 3 4 6 7 10 14 , 3
# 2 4 6 7 10 14 , 3
# 2 3 4 6  10 14 , 3
# 2  4 6  10 14 , 3
# 2  6  10 14 , 3
# 2 6 10 14