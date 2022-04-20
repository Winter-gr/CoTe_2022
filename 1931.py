N = int(input())


times = [0]
cnt = 0

for i in range(N) :
	start, finish = map(int, input().split())
	if times[-1] <= start :
        cnt += 1
        times.append(finish)
        
print(cnt)
