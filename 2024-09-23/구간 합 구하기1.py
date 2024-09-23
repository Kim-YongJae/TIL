N = int(input())
numbers = list(map(int, input().split()))
i, j = map(int, input().split())

sum_list = [0]
sum = 0

for a in numbers:
    sum += a
    sum_list.append(sum)
    
sum_array = sum_list[j] - sum_list[i-1]
print(sum_array)

# 여러번의 질문을 입력할 수 있도록 변형
# N, M = map(int, input().split())
# numbers = list(map(int, input().split()))

# sum_list = [0]
# sum = 0

# for a in numbers:
#     sum += a
#     sum_list.append(sum)
    
# for b in range(M):
#     i, j = map(int, input().split())
#     sum_array = sum_list[j] - sum_list[i-1]
#     print(sum_array)