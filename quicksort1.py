def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]

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

    return quicksort(left) + middle + quicksort(right)

n = int(input("Enter number of elements: "))

user_list = []
print("Enter the elements:")

for i in range(n):
    num = int(input())
    user_list.append(num)

# Sorting
sorted_list = quicksort(user_list)

print("Sorted list:", sorted_list)