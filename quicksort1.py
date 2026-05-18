def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    right = []
    middle = []
    left = []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            middle.append(element)
    
    return quicksort(left) + middle + quicksort(right)
