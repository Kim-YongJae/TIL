# 매개변수로 전달 받은 숫자까지 존재하는 모든 종말의 수를 담은 배열을 반환하시오.
# 종말의 수: 6이 적어도 3개 이상 연속으로 들어가는 수

def doom_day(n): # n은 최대 숫자
    doom = []
    for i in range(1, n+1):
        if '666' in str(i):
            doom.append(i)
        
    return doom

'''강사님 풀이 n은 갯수
def doom_day(n):
    cnt = 0
    doom = 666
    arr = []
    
    while True:
        if '666' in str(doom):
            cnt += 1
            arr.append(doom)
        if cnt == n:
            break
        doom += 1
    return arr
'''




# 전달 받은 배열들의 요소 중 7요소의 부분합이 100이 되게끔 하는 로직을 작성하고
# 부분합이 100이 되는 요소 7개를 배열로 반환하시오
def dwarf(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if sum(array)-array[i] > 100:
                sum1 = sum(array)-array[i]
                if sum1 - array[j] > 100:
                    pass
                elif sum1-array[j] == 100:
                    array.remove(array[i])
                    array.remove(array[j-1])
                    
                    return array, sum(array)
            
'''강사님 풀이
def dwarf(array):
    s = sum(arr)
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if s - arr[i] - arr[j] == 100:
                a, b = arr[i], arr[j]
                arr.remove(a)
                arr.remove(b)
                return arr
    return arr
'''