# 1. 투 포인터
- sum > N: sum -= start_index; start_index++;
- sum < N: end_index++; sum += end_index;
- sum == N: end_index++; sum += end_index; count++;