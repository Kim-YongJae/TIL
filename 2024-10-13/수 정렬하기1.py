n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())
    
for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            b = a[j]
            a[j] = a[j+1]
            a[j+1] = b

for i in range(n):
    print(a[i])