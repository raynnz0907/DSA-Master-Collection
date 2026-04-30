def linearsearch(list1,target):
    flag = 0
    for i in range(len(list1)):
        if list1[i] == target:
            flag = 1
            print("Found")
    if flag == 0:
        print("Target not found")

list1 = [15,62,14,7,1,6,3]
target = 98
linearsearch(list1,target)    