# 매개변수로 금액을 전달하면 해당 금액을 최소한의 동전 개수로 구할 수 있는 동전 조합을 구하는 함수를 작성하시오
# 동전 종류: 500, 100, 50, 10, 1
# ex) 금액: 3465
#     결과: {500: 6, 100:4, 50: 1, 10: 1, 1: 5}

def coin_combi(change):
    '''
    res={}
    a= change//500
    res[500]=a
    b= (change-a*500)//100
    res[100]=b
    c= (change-a*500-b*100)//50
    res[50]=c
    d= (change-a*500-b*100-c*50)//10
    res[10]=d
    e= (change-a*500-b*100-c*50-d*10)//1
    res[1]=e
    
    print(res)
    '''
    
    coins = [500, 100, 50, 10, 1]
    res = {}
    
    for coin in coins:
        res1 = change//coin
        change = change - res1*coin
        res[coin]=res1
        
    print(res)
    
    '''강사님 코드
    coins = {500:0, 100:0, 50:0, 10:0, 1:0}
    
    for coin in coins:
        coins[coin] = change//coin
        change %= coin
        
    print(coins)
    '''
coin_combi(3465)