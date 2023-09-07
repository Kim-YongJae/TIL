# 정렬된 배열 두 개를 매개변수로 받아 하나의 정렬된 배열로 합쳐주는 함수 / 메모리에 많은 배열이 남아 메모리를 많이 차지한다.
# [1,5,7,13] [2,4,9,12,15]
def merge(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
            
    if i < len(arr1):
        res += arr1[i:len(arr1)]
    else:
        res += arr2[j:len(arr2)]
        
    return res

def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        mid = n//2
        arr1 = mergesort(arr[0:mid])
        arr2 = mergesort(arr[mid:n])
        return merge(arr1,arr2)