def bubblesearch(arr):
    n = len(arr)

    for i in range (n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]


def seleectionsort(arr):
    for i in range(len(arr)):
        min_val = min(arr[i:])
        min_index = arr.index(min_val)
        arr[i],arr[min_index] = arr[min_index], arr[i]
