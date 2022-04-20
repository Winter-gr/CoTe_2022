from sys import stdin

N = int(input())
times = list(map(int, input().split()))

# 퀵 정렬
times.sort()

sum = 0
answer = 0
for time in times :
    # n 번째 사람이 걸리는 시간  
    sum += time
    # 걸리는 시간의 총합
    answer += sum
    
print(answer)

# 성공
