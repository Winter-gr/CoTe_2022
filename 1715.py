import heapq

N = int(input())

nums = []
heapq.heapify(nums)
ans = 0

for i in range(N) :
	heapq.heappush(nums, int(input()))

while len(nums) >= 2 :
	first = heapq.heappop(nums)
	second = heapq.heappop(nums)
	sub = first + second
	ans += sub
	heapq.heappush(nums, sub)

print(ans)

# 성공