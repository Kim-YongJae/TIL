from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
queue = PriorityQueue()

for i in range(n):
    a = int(input())
    if a == 0:
        if queue.empty():
            print('0\n')
        else:
            b = queue.get()
            print(str(b[1])+'\n')
    else:
        queue.put((abs(a), a))