def partition2(arr, low, high):
    pivotitem = arr[low]
    i = low + 1
    j = high
    
    while (i <= j):
        while arr[i] < pivotitem:
            i += 1
            if i > high: break
            
        while arr[j] > pivotitem:
            j -= 1
            if j < low: break
            
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    pivotpoint = j
    arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low]
    return pivotpoint

def quicksort2(arr, low, high):
    if low <= high:
        pivotpoint = partition2(arr, low, high)
        quicksort2(arr, low, pivotpoint-1)
        quicksort2(arr, pivotpoint+1, high)