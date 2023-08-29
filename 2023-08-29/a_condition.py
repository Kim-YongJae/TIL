# 세 수 중 최대값 구하기
def max(a,b,c):
    max=a
    if(b>max):
        max=b
    elif(c>max):
        max=c
    return max

print(max(50,255,30))


# 세 수 중 최소값 구하기
def min(a,b,c):
    min=a
    if(b<min):
        min=b
    elif(c<min):
        min=c
    return min
print(min(50,255,30))

# 세 수 중 중간값 구하기
def med(a,b,c):
    if b<=a<=c or c<=a<=b:
        med=a
    elif a<=b<=c or c<=b<=a:
        med=b
    else:
        med=c
    return med
print(med(50,255,30))