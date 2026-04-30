def binarysearch(list,target):
    flag = 0
    low = 0
    high = len(list) - 1
    
    while high >= low:
        mid = (low + high)// 2

        if list[mid] == target:
            print("Element found at index",mid)
            flag = 1
            break 
        elif list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    if flag == 0:
        print("Not found")




list = [1,2,3,4,5,6,7,8,9,10]
target = 2
binarysearch(list,target)
