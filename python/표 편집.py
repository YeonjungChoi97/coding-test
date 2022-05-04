#very difficult, had to recap on dllist for around 2-3 hrs
#took ~ 3.5 ish hrs
#link: https://programmers.co.kr/learn/courses/30/lessons/81303

# Create the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
def solution(n, k, cmd):
    
    node_list = [Node("O") for _ in range(n)]
    for i in range(1,n):
        node_list[i-1].next = node_list[i]
        node_list[i].prev = node_list[i-1]
        
        
    deleted_node = []
    current_node = node_list[k]
    
    
    for i in cmd:
        
        i = i.split(" ")
        if i[0] == "U":
            for i in range(int(i[1])):
                current_node = current_node.prev
        elif i[0] == "D":
            for i in range(int(i[1])):
                current_node = current_node.next
        elif i[0] == "C":
            current_node.data = "X"
            deleted_node.append(current_node)

            upper = current_node.prev
            lower = current_node.next
            if upper:
                upper.next = lower

            if lower:
                lower.prev = upper
                current_node = lower
            else:
                current_node = upper
        else:
            undo = deleted_node.pop()
            undo.data = "O"
            upper = undo.prev
            lower = undo.next
            if upper:
                upper.next = undo
            if lower:
                lower.prev = undo

    answer = ""
    
    for i in range(len(node_list)):
        answer += node_list[i].data
    
    
    return answer
