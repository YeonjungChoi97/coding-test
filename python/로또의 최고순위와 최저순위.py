#05/07/2022 
# quick 10 min quiz,short and sweet
# before meeting with Jieun and Heain
#link: https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3#_=_

def solution(lottos, win_nums):
    match = set(lottos) & set(win_nums)

    if len(match) >= 2:
        min_win = 7-len(match)
    else:
        min_win = 6
    print(min_win)
    
    unknown = lottos.count(0)
    
    if unknown > 0 and unknown < 6 :
        max_win = min_win - unknown
    elif unknown == 6:
        max_win = 1
    else:
        max_win = min_win
    
    print(max_win)
    
    answer = [max_win,min_win]
    return answer
