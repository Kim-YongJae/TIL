n = int(input()) #과목의 갯수 입력
score = list(map(int, input().split())) #점수 입력
sum = 0
max = max(score)

for i in score:
    sum += (i/max)*100
    
average = sum/n

print(average)