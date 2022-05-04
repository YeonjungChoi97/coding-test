#link: https://programmers.co.kr/learn/courses/30/lessons/81303
# 테스트 케이스는 통과하였지만, 제출후 반 이상의 케이스 failed. gotta check up.

def up(l,i,n):
    
    while n > 0:
        if l[i] == "O":
            n -= 1
            i -= 1
        else:
            i -= 1

    
    return i

def down(l,i,n):
    
    while n > 0:
        if l[i] == "O":
            n -= 1
            i += 1
        else:
            i += 1      
    return i

def c(i_list,index, recent_delete):
    
    recent_delete.append(index)
    i_list[index] = "X"
    
    
    if len(i_list) == (index+1):
        index -=1
    else:
        index += 1     
    
    return i_list, index, recent_delete

def undo(i_list, recent_delete):
    
    i_list[recent_delete[len(recent_delete)-1]] = "O"
    recent_delete.pop(len(recent_delete)-1)
    
    return i_list, recent_delete
    


def solution(n, k, cmd):
    i_list =["O"]*n
    recent_delete = []
    index = k
    
    for i in cmd:
        i = i.split(" ")

        try:
            if i[0] == "D":
                index = down(i_list,index, int(i[1]))
            elif i[0] == "C":
                i_list, index, recent_delete = c(i_list, index, recent_delete)
            elif i[0] == "U":
                index = up(i_list, index, int(i[1]))
            else:
                i_list, recent_delete = undo(i_list, recent_delete)
        except:
            print("error")
    answer = ''.join(i_list)
    return answer
