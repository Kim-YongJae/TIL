# 1. 구간 합 구하기2
- 구간 합을 구하기 위해서는 '합 배열'을 먼저 구해야한다.
- 배열이 행만 있다면 '합 배열'이 S라고 한다면 S를 [0]에서 부터 시작하여 데이터의 합을 추가한 것과 같이 열이 존재한다면 첫번째 열(index가 0인 열)에도 [0]부터 시작한다.
- [0]*3 = [0, 0, 0] , [0]+[1, 2] = [0, 1, 2]
- [[0]*5 for_ in range(5)]는 아래와 같다.
-   [[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]