def solution(numbers):

    strings = map(str, numbers)
    reverse_answer = sorted(strings, key=lambda x : x[::-1])
    
    answer = ''.join(reverse_answer[::-1])    
    return answer

