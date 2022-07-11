import heapq

N = int(input())

nums = []
heapq.heapify(nums)
ans = 0

# 한 줄 씩 입력 받으면서 정렬
for i in range(N) :
	heapq.heappush(nums, int(input()))

# 수를 두 걔씩 꺼내야 하므로 힙에 요소가 2개보다 큰 것을 조건으로 한다.
while len(nums) >= 2 :
	# 첫번쨰로 작은 수와 두번쨰로 작은수 꺼내기
	first = heapq.heappop(nums)
	second = heapq.heappop(nums)
	# 합(비교)하기
	sub = first + second
	# 비교한 횟수를 정답에 추가하기
	ans += sub
	# 카드 묶음 개수를 다시 힙에 저장
	heapq.heappush(nums, sub)

print(ans)

# 성공