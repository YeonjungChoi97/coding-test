#link: https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    
    action = []
    user = {}
    #dictonary를 쓰는 이유는, user 의 action 에 불구하고 (enter, change) 마지막 유저네임이 파이널 유저네임일것.
    
    for i in record:
        i = i.split(" ")
        if len(i) > 2:
            user[i[1]] = i[2]
        action.append(i[0:2])
    answer = []
    for i in action:
        user_name = user[i[1]]
        if i[0] == "Enter":
            a = user_name + "님이 들어왔습니다."
            answer.append(a)
        elif i[0] == "Leave":
            a = user_name + "님이 나갔습니다."
            answer.append(a)

    
    return answer
