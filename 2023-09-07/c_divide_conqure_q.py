# 거듭제곱 최적화
# 매개변수 A,B를 받아 A를 B번 곱한 값을 반환한느 함수를 작성하시오.
# 해당 함수의 시간복잡도는 O(logN)입니다.
# B가 짝수 일 경우 A^B=A^(B//2)*A^(B//2)
# B가 홀수 일 경우 A^B=A^(B//2)*A^(B//2)*A
# 로 나타낼 수 있다.




def pow(a,b):
    if b== 0:
        return 1
    if b%2 == 0:
        res = pow(a, b // 2)
        return res*res
    else:
        res = pow(a, b // 2)
        return res*res*a

            
print(pow(2,10))