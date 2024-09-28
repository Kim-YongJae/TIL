import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
n_s = list(map(int, input().split()))
n_s.sort()
i = 0
j = n-1
count = 0

while i < j:
    if n_s[i] + n_s[j] < m:
        i += 1
    elif n_s[i] + n_s[j] >m:
        j -= 1
    else:
        count += 1
        i += 1
        j += 1
        
print(count)