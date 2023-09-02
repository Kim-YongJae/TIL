class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return self.data
        
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    # 가장 위에 있는 데이터를 꺼내고 삭제        
    def pop(self):
        if self.top is None:
            return None
        
        node = self.top
        self.top = node.next
        return node.data
    
    # 가장 위에 있는 데이터를 꺼내기만 함
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def __str__(self):
        if self.top is None:
            return '빈 스택입니다.'
        
        link = self.top
        res = '[ top << ' + str(link.data)
        
        while link.next is not None:
            temp = link.next
            res += ', ' + str(temp.data)
            link = temp
            
        res += ' ]'
        return res