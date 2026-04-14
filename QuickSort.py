def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left = []
    right = []
    middle = []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            middle.append(element)
        
    return quick_sort(left) + middle + quick_sort(right)

arr = [1,5,7,8,9,0,3,2]
print(quick_sort(arr))
