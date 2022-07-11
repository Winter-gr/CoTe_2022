from collections import deque
itr = int(input())

for i in range(itr):
    # n - 문서의 개수 
    # m - 확인하고 싶은 문서의 위치
    n, m = map(int, input().split())
    # 문서 입력 받기
    papers = list(map(int, input().split()))
    # papers 리스트를 큐로 만든다
    papers_q = deque(papers)
    # 우선순위가 높은 문서부터 가져오는 큐를 만든다.
    papers.sort(reverse=True)
    priority_q = deque(papers)
    
    cnt = 0
    while papers_q:
        # 문서와 문서의 우선순위를 함께 확인한다.
        paper = papers_q.popleft()
        priority = priority_q.popleft()
        # 문서가 가장 높은 우선순위를 가진 경우
        if paper == priority:
            # 문서를 출력한 것으로 보고, 인쇄한 횟수를 증가시킨다.
            cnt+=1
            # 확인하고 싶은 문서가 출력되었다면 break 아니라면 확인하고 싶은 문서의 위치 -1
            if m == 0:
                break
            else :
                m -= 1
        # 문서의 우선순위가 낮아서 출력하지 못하는 경우
        else :
            # 문서를 가장 마지막순서로 배치한다.
            papers_q.append(paper)
            priority_q.appendleft(priority)
            # 확인하고 싶은 문서의 위치 갱신
            if m == 0 :
                m = len(papers_q)-1
            else :
                m -= 1
    print(cnt)

    #성공