# Using indexing from 1
# O(nlogn)


def create_heap(arr, i = 2, j = 2):
    if (i == len(arr) + 1):
        return arr
    if (j <= 1):
        i += 1
        j = i
        create_heap(arr, i , j)
    else:
        p_j = int(j/2)
        if (arr[p_j -1 ] < arr[j -1]):
            print("if 3 - swaping ", arr[p_j - 1], arr[j - 1])
            arr[p_j - 1], arr[j - 1] = arr[j - 1], arr[p_j - 1]
            create_heap(arr, i, p_j)
        else:
            print("if 3 - not swapping", arr[p_j - 1], arr[j - 1])
            i += 1
            j = i
            create_heap(arr, i , j)

    return arr


# op = create_heap([10, 20, 15, 30, 40])
# print("op = ", op)
