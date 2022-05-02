#5월 2일 월요일
#문제 풀이시간: 아마 1시간 정도 ㅜㅜ
#링크: https://programmers.co.kr/learn/courses/30/lessons/72411

import itertools 

def split(word):
    return list(word)

def solution(orders, course):
    combs = []
    orders_as_list = []
    
    
    for j in orders:
        j = split(j)
        j = sorted(j)
        orders_as_list.append(j)
    for i in course:
        for j in orders_as_list:
            combs.extend([''.join(t) for t in itertools.combinations(j,i)])
    combs = list(set(combs))
        

    dict_c = dict.fromkeys(combs, 0)
    for i in combs:
        i_s = set(split(i))
        for j in orders:
            j_s = set(split(j))
            if i_s.issubset(j_s):
                dict_c[i] +=1
                
 
    final = []
    for i in course:
        length_value = {key:value for (key, value) in dict_c.items() if (len(key) == i and value >= 2)}
        if len(length_value) > 0:
            max_value = max(length_value.values())
            a = [k for k,v in length_value.items() if v == max_value]
            final.extend(a)
            
    final = sorted(final)

    answer = final
    return answer
