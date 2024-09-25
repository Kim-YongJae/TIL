import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

S = [0]*n
C = [0]*m
count = 0
S[0] = numbers[0]

for i in range(1, n):
    S[i] = S[i-1] + numbers[i]

for i in range(n):
    divide = S[i] % m
    if divide == 0:
        count += 1
    C[divide] += 1

for i in range(m):
    if C[i] > 1:
        count += (C[i]*(C[i]-1)//2)
        
print(count)