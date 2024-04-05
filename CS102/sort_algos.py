
# Both sorting methods sort from highest to lowest since I want the most popular of each catagory at the front

def bubblesort(array):
    for idx_outer in range(len(array)):
        for idx_inner in range(len(array) - idx_outer - 1):
            if array[idx_inner][1] < array[idx_inner + 1][1]:
                array[idx_inner], array[idx_inner +1 ] = array[idx_inner + 1], array[idx_inner]

    return array

def mergesort(array):
    if len(array) <= 1:
        return array
    
    mid_idx = len(array)//2
    left_split = array[:mid_idx]
    right_split = array[mid_idx:]

    left_sort = mergesort(left_split)
    right_sort = mergesort(right_split)

    out_array = []
    while (left_sort and right_sort):
        if left_sort[0][1] > right_sort[0][1]:
            out_array.append(left_sort[0])
            left_sort.pop(0)
        else:
            out_array.append(right_sort[0])
            right_sort.pop(0)

    if left_sort:
        out_array += left_sort
    if right_sort:
        out_array += right_sort
    
    return out_array