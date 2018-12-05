
def quicksort(arr, left, right):
    if (left < right):
        part_index = partition(arr, left, right)
        quicksort(arr, left, part_index-1)  # Recurse using left of partition
        quicksort(arr, part_index+1, right) # Recurse using right of partition

def partition(arr, left, right):
    pivot = arr[right]  # Choose last element of left...right as pivot
    i = left - 1
    for j in range(left, right):  # Iterate through element before right
        if (arr[j] <= pivot):
            i += 1
            # Swap arr[i] with arr[j]
            arr[i], arr[j] = arr[j], arr[i]

        
    # Swap arr[i+1] with the pivot
    # then everything to left of pivot is <= pivot
    # and everything to right of pivot is > pivot
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

l = [54, 14, 60, 77, 75, 36, 3, 4, 100, 50, 39, 70, 47, 43, 65, 41, 37, 28, 14, 28, 22, 2, 1, 3, 1, 13, 14, 24, 76, 42, 59, 57, 33, 65, 62, 18, 9, 35, 71, 54, 43, 93, 12, 81, 31, 13, 96, 74, 63, 6]

print(l)
quicksort(l,0,len(l)-1)
print(l)
