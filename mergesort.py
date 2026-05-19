def mergesort(list):
    if len(list) <= 1:
        return list
    
    pivot = len(list) // 2
    left_half = mergesort(list[pivot:])
    right_half = mergesort(list[:pivot])

    return merger(left_half,right_half)

def merger(a,b):
    merge = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merge.append(a[i])
            i+= 1
        else:
            merge.append(b[j])
            j+=1
        
    merge.extend(a[i:])
    merge.extend(b[j:])

    return merge

