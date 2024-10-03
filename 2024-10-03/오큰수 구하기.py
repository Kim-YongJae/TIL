n = int(input())
num = list(map(int, input().split()))

answer = [0]*n
s = []

for i in range(n):
    while s and num[s[-1]] < num[i]:
        answer[s.pop()] = num[i]
    s.append(i)
    
while s:
    answer[s.pop()] = -1

result = ""

for i in range(n):
    result += str(answer[i])+" "
    
print(result)