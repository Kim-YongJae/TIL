import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[0]*(N+1)]
B = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

for i in range(1, N+1):
    for j in range(1, N+1):
        B[i][j] = B[i-1][j] + B[i][j-1] - B[i-1][j-1] + A[i][j]

for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    answer = B[X2][Y2] - B[X2][Y1-1] - B[X1-1][Y2] + B[X1-1][Y1-1]
    print(answer)