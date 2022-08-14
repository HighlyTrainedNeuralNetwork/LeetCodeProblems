# Mimicking bubble sort.

def pancakeSort(arr):
    flips = []
    for i in range(len(arr), 0, -1):
        cur_index = arr.index(i)
        if cur_index != i - 1:
            if cur_index != 0:
                flips.append(cur_index + 1)
                suffix = arr[cur_index + 1:]
                prefix = arr[:cur_index + 1][::-1]
                arr = prefix + suffix

            flips.append(i)
            suffix = arr[i:]
            prefix = arr[:i][::-1]
            arr = prefix + suffix
    return flips

arr = [3,2,4,1]
print(pancakeSort(arr))