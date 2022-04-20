n = int(input())
tower = [0] + list(map(int, input().split()))

answer = [0]

for i in range(1, 1+n):
    if tower[i] > tower[i-1]: 
        answer.append(i)
        print(answer[0])
    elif tower[i] < tower[i-1]:
        answer.append()
    

