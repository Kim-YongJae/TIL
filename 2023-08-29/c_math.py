from math import sqrt

# 매개변수로 전달받은 숫자가 소수인지 판별하는 함수를 만드시오
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def is_prime2(n):
    for i in range(2, int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True

# 2부터 매개변수로 입력받은 값 사이에 존재하는 소수를 구해 리스트로 반환하는 함수를 작성하시오
def is_prime3(n):
    primes=[]
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)
    return primes

# 두 수의 최대공약수를 구하는 함수를 작성하시오
def gcd1(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
        
# 유클리드 호제법
def gcd2(a,b):
    while b>0:
        a,b=b,a%b
    return a
# G가 a와 b의 최대공약수 일 때 a=MG, b=NG라 표현 가능
# a>b일 때
# a mod b
# a=bq+r (q는 몫, r은 나머지)
# MG=NGq+r
# r=MG-NGq
# r=G(M-Nq) --> r은 G의 배수
# G의 배수인 두 수의 나머지는 G의 배수이므로 b와 r의 나머지 연산 결과도 G의 배수
# b mod r
# b=NG
# r=PG
# c=QG
# ...
# x=XG
# y=G
# z=0 --> 나머지

# 최소공배수
def lcm1(a,b):
    return (a*b)/gcd1(a,b)
    #return gcd1(a,b)*a/gcd1(a,b)*b/gcd1(a,b)