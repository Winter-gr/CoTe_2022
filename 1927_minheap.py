from sys import stdin
import heapq

# n = int(input())
n = int(stdin.readline())

minheap = []
answer = []
heapq.heapify(minheap)

for i in range(n):
    num = int(stdin.readline())
    if num != 0:
        heapq.heappush(minheap, num)
    elif minheap: 
        answer.append(heapq.heappop(minheap))
    else:
        answer.append(0)

for i in answer:
    print(i)
