from sys import stdin

N = int(input())
times = list(map(int, input().split()))

times.sort()

sum = 0
answer = 0
for time in times :  
    sum += time
    answer += sum
    
print(answer)

# 성공
