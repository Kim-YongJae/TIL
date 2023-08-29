# 1+2+3+4+...+n
# 매개변수로 n을 입력받아 출력

def q1(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
        if i<n:
            print(i,'+ ',end='')
        else:
            print(i,'= ',end='')
    print(sum)


n=int(input('n을 입력하시오:'))
q1(n)

# 다이아몬드 별찍기
# 사용자로 부터 2이상의 자연수를 입력 받아
# 한 변의 길이가 사용자의 입력값인 다이아몬드를 그려보시오
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

#  *
# ***
#  *

#   *
#  ***
# *****
#  ***
#   *
def print_diamond(n):
    for i in range(n):
        print(' '*(n-i-1)+'*'*(i*2+1))
    for i in range(n-1):
        print(' '*(i+1)+'*'*((n-i-1)*2-1))
        
n=int(input('n의 값:'))
print_diamond(n)

'''임효민님 풀이
def print_diamond(cnt):
    for i in range(cnt):
        for j in range(cnt-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()
    for i in range(cnt-2, -1, -1):
        for j in range(cnt-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()
        
print_diamond(cnt)
'''

'''강사님 풀이
*의 개수는 홀수로 증가 2n-1
공백의 개수 cnt-n
n은 1부터 1씩 증가하는 자연수
cnt는 입력값
--------
*의 개수는 홀수로 감소 2n-1
공백의 개수는 1부터 1씩 증가하는 자연수
n은 cnt부터 1씩 감소하는 자연수

def print_diamond(cnt):
    for i in range(cnt):
        n=i+1
        for j in range(cnt-n):
            print(" ", end="")
        for k in range(2*n-1):
            print("*", end="")
        print()
        
    white_space=1
    for i in range(cnt-1,-1,-1):
        for j in range(white_space):
            print(" ", end="")
        white_space+=1
        for k in range(2*i-1):
            print("*", end="")
        print()
        
print_diamond(10)
'''
