# 탑다운
def fibo_recur(n, memo=[None for _ in range(100)]):
    if n == 0:
        return 0
    
    if n==1 or n==2:
        return 1
    
    if memo[n] is not None:
        return memo[n]
    
    memo[n] = fibo_recur(n-1, memo)+fibo_recur(n-2, memo) 
    # fibo_recur(n-1, memo)부터 하고 fibo_recur(n-2, memo)를 계산한다. memo로 저장하기 때문에 fibo_recur(n-1, memo)를 계산할 때 얻은 값을 바탕으로 fibo_recur(n-2, memo)의 값은 계산하지 않고 불러온다.
    return memo[n]
    
print(fibo_recur(10))

# 바텀업
def fibo_dp2(n):
    tmp = []
    tmp.append(1)
    tmp.append(1)
    
    if n < 2:
        return tmp[-1]
    
    for i in range(2, n):
        tmp.append(tmp[i-2]+tmp[i-1])
        
    return tmp[-1]

print(fibo_dp2(10))