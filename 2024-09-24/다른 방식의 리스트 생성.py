A1 = [[2 for _ in range(5)] for _ in range(5)]
A1[0][0] = 9
print(A1)

A2 = [[2]*5 for _ in range(5)]
A2[0][0] = 9
print(A2)

# 위의 두 방법 모두 각 행이 독립적인 리스트!