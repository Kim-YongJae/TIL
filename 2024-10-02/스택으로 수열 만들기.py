n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    if a[i] >= num:
        while a[i] >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        
        if n > a[i]:
            print("no")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)