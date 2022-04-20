def solution(lottos, win_nums):
    answer = []
    ze
    lotto = set(lottos)
    win_num = set(win_nums)
    
    if len(lotto) <

    zeros = 6 - (len(lotto) - 1)

    count = 7 - len(lotto & win_num)
    if count == 7 :
        count = 6 

    answer.append(count - zeros)
    answer.append(count)
    
    return answer