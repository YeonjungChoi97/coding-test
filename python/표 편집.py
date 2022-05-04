#link: https://programmers.co.kr/learn/courses/30/lessons/81303
## runtime errors :/ code efficiency apparently 0

# Create the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
# Create the doubly linked list class
class doubly_linked_list:
    def __init__(self):
        self.head = None

    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return
    
    def final(self, node):
        str_final = ""
        while (node is not None):
            
            str_final = str_final + node.data 
            last = node
            node = node.next
        return str_final
    
    
        

    
def solution(n, k, cmd):
    
    dlist = doubly_linked_list()
    first_node = "O"
    dlist.append(first_node)
    current_node = first_node
    deleted_node = []
    
    #initialising linked list
    while n > 1:
        next_node = "O"
        dlist.append(next_node)
        current_node = next_node
        n -= 1 
    
    
    #place the node to k position
    current_node = dlist.head

    while k > 0:
        current_node = current_node.next
        k -= 1
    
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
            if lower:
                upper.next = lower
                lower.prev = upper
                current_node = lower
            else:
                upper.next = lower
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

    while len(deleted_node) > 0:
        undo = deleted_node.pop()
        upper = undo.prev
        lower = undo.next
        upper.next = undo
        lower.prev = undo

    answer = dlist.final(dlist.head)

    
    
    return answer
