def selection_sort(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
                
        arr[i], arr[min] = arr[min], arr[i]
        
    return arr

print(selection_sort([8,9,7,15,6,24,2,37]))

'''
def selection_sort(arr):
    for p in range(len(arr)-1):
        min = p

        for i in range(p,len(arr)):
            if arr[min]>arr[i]:
                min = i
                
        arr[p], arr[min] = arr[min], arr[p]
        
    return arr
'''