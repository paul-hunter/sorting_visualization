
def quicksort(arr, left, right):
    if (left < right):
        part_index = partition(arr, left, right)
        print("partition: ", part_index)
        print("left: ", arr[:part_index])
        print("right: ", arr[part_index:])
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

arr = [5,6,1,3,8,-212,1,-10,2,9,2,1,0]
print(arr)
quicksort(arr,0,len(arr)-1)
print(arr)
