class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # 다음 노드의 주소를 저장
        
# __메서드__ (매직메서드, 던더메서드)
# 파이썬에서 제공해주는 내장 함수 또는 구문에서 호출하기 위해 작성하는 함수
        
# 덕타이핑: 객체의 속성 및 메서드의 집합이 객체의 타입을 결정하는 것
# 만약 어떤 새가 오리처럼 걷고, 헤엄치고, 소리를 낸다면 그 새를 오리라고 부를 수 있다.
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    # print 함수에 객체를 매개변수로 전달할 경우 출력될 문자열을 반환하는 매직메서드
    def __str__(self):
        node = self.head
        if node is None : return '비어있습니다'
        res = '['
        while node.next:
            res+=str(node.data)+', '
            node = node.next
        res+=str(node.data)+']'
        
        return res
    # 매개변수로 전달받은 데이터를 리스트에 추가
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            prev = self.head
            
            while prev.next:    # next가 None인 Node를 탐색
                prev=prev.next
                
            prev.next=node  # next가 None인(현재 마지막 요소인) 노드에 새로운 도드를 링크
            
        self.length += 1
        


    #매개변수로 전달받은 데이터를 리스트의 가장 앞에 추가
    def prepend(self, data):
        node=Node(data) # 데이터로 새로운 노드 생성
        node.next = self.head   # 현재 노드가 가리키는 다음 노드(새로운 노드)가 head(첫 번째 노드)가 된다
        self.head = node    # 첫 번째 노드가 새로운 노드가 된다
        self.length += 1    # 리스트의 길이 증가
        
    def insert(self, i, data):
        if i<0:
            raise IndexError('인덱스는 음수 일 수 없습니다.')
        if i==0:
            self.prepend(data) 
            return 
        if i>=self.length:
            self.append(data)
            return
        
        node=Node(data)
        prev = self.head
        
        for _ in range(i-1):
            prev = prev.next
            
        node.next = prev.next
        prev.next = node
        self.length += 1
    
    # 가장 뒤에 있는 데이터를 반환하고 삭제
    def pop(self):
        node = self.head
        if node is None:
            return None
        
        # 노드가 하나 있는 경우
        if node.next is None:
            self.head = None
            self.length -= 1
            return node
        
        prev = node
        while node.next:
            prev = node
            node = node.next
            
        prev.next = None
        self.length -=1
        return node.data
    
    # 첫번재 데이터를 반환하고 삭제
    def popleft(self):
        node = self.head
        if node is None:
            return None
        
        self.head = self.head.next
        self.length -= 1
        return node.data
    
    # 매개변수로 전달받은 data를 삭제하고 성공여부를 T/F로 반환
    def remove(self, data):
        node = self.head
        if node.data == data:
            self.popleft()
            return True
        
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                self.length -= 1
                return True
            
            node = node.next                      
        return False
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    '''강사님 풀이
    def reverse(self):
        if self.length<=1:
            return
            
        prev = None
        
        while self.head.next:
            tmp = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = tmp
            
        self.head.next = prev
    '''
    
    # ---------------------------------------
    
    def __iter__(self):
        return LinkedList.Iterator(self.head)
        
        
    class Iterator:
        def __init__(self, node):
            self.node = node
            self.call_cnt=1
            
        def __iter__(self):
            return self
        
        def __next__(self):                        
            if self.node is None:
                raise StopIteration
            
            print(f'{self.call_cnt}번째 호출입니다. {self.node.data}')
            
            data = self.node.data
            self.node = self.node.next
            self.call_cnt += 1
            return data