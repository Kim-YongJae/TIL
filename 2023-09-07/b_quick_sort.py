def partition(arr, low, high):
    pivotitem = arr[low]
    j = low
    for i in range(low+1, high+1):
        if arr[i] < pivotitem:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    pivotpoint = j
    arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low]
    return pivotpoint

def quicksort(arr, low, high):
    if low < high:
        pivotpoint = partition(arr, low, high)
        quicksort(arr, low, pivotpoint-1)
        quicksort(arr, pivotpoint+1, high)