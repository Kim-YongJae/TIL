import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

num.sort()
count = 0

for a in num:
    i = 0
    j = n-1
    
    while i < j:
        if num[i] + num[j] < a:
            i += 1
        elif num[i] + num[j] > a:
            j -= 1
        else:
            count += 1
            i += 1
            j -= 1
            break

print(count)