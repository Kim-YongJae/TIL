# n개의 정수로 이루어진 임의의 수열이 주어진다.
# 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
# 단, 수는 한 개 이상 선택해야 한다.
# 입력: [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
# 출력: 33

def sub_sum(arr):
    sum_array = [arr[0]]
    sum = arr[0]
    max_sum = arr[0]
    for i in range(1,len(arr)):
        sum = max(arr[i], sum + arr[i])
        sum_array.append(sum)
        max_sum = max(max_sum, sum)
        
    return f'sum_array: {sum_array}, max_sum: {max_sum}'


'''강사님 문제
def sub_sum(arr):
    sum_arr = [arr[0]]
    
    for e in arr[1:]:
        sum_arr.append(max(sum_arr[-1]+e, e))
        
    return max(sum_arr)
'''
        

arr = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
print(sub_sum(arr))