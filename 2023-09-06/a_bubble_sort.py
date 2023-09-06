# bubble sort: 인접한 배열의 두 수를 선택해, 그 두 수가 정렬되어 있지 않다면 두 수를 정렬하는 방식

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1): # for j in range(len(arr)-1):
            if arr[j]<arr[j+1]:
                pass
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr    
    

print(bubble_sort([5,8,12,34,3,1]))

'''
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr
    
    
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr
    
오름차순    
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        flag = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            return arr
                
    return arr
'''
'''내림차순
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        flag = False
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            return arr
                
    return arr
'''