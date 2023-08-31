class Node:
    def __init__(self, key: str, data):
        self.key = key
        self.data = data
        self.next = None
        
    def __hash__(self):
        return 31 * sum([ord(s) for s in self.key])
    
    def __eq__(self, other):
        return self.key == other.key
    
    def __str__(self):
        return '[key= ' + self.key + ': data= ' + str(self.data) + ']'
    
    
class DuplicatedKey(RuntimeError):
    pass

        
class HashTable:
    def __init__(self, length=30):
        self.max_len = length
        self.table = [None for _ in range(self.max_len)]
        self.length = 0
        
    def __str__(self):
        res=''
        for link in self.table:
            if link is None: continue
            
            while(True):
                res += str(link)
                if link.next is None:break
                link = link.next
                
        return res
        
    def hash(self, node):
        return hash(node) % self.max_len
    
    def __add(self, link, node):
        if link == node:
            raise DuplicatedKey
        
    def __set(self, link, node):
        if link == node:
            link.data = node.data
            raise DuplicatedKey
    
    def __add_data(self, key:str, data, fn):
        if type(key) is not str:
            raise TypeError('문자열만 key로 사용이 가능합니다.')
        
        node = Node(key, data)
        index = self.hash(node)
        
        if (self.table[index] is None):
            self.table[index] = node
        else:
            link = self.table[index] # 해당 인덱스에 저장된 첫번재 노드
            
            while(True):
                
                try:
                    fn(link, node)
                except:
                    return # __add와 __set에 return을 붙이면 while문이 끝나는게 아니라 __add와 __set이 끝나는 것이기 때문에 return을 따로 빼서 써준다.
                
                if link.next is None:
                    link.next = node
                    break
                
                link = link.next
                
        self.length += 1
        
        
    # 키를 해싱해 data를 저장
    # 사용자가 이미 등록한 키로 다시 데이터를 저장 할 수 없음
    def add(self, key: str, data):
        '''
        if type(key) is not str:
            raise TypeError('문자열만 key로 사용이 가능합니다.')
        
        node = Node(key, data)
        index = self.hash(node)
        
        if (self.table[index] is None):
            self.table[index] = node
        else:
            link = self.table[index] # 해당 인덱스에 저장된 첫번재 노드
            
            while(True):
                if link == node: # 만약 link의 key값과 node의 key값이 같다면 데이터를 추가하지 않고 return
                    return
                
                if link.next is None:
                    link.next = node
                    break
                
                link = link.next
                
        self.length += 1
        '''
        
        # 파이썬의 함수는 1급 객체
        # 1급 객체: 값으로 다루어 질 수 있음
        # 매개변수로 넘길 수 있고, 변수에 담을 수 있고, return값으로 쓸 수 있다.
        self.__add_data(key, data, self.__add)
    
        
    # 키를 해싱해 data를 저장
    # 사용자가 이미 등록한 키로 접근해 데이터를 수정(데이터를 덮어씀)
    def set(self, key: str, data):
        '''
        if type(key) is not str:
            raise TypeError('문자열만 key로 사용이 가능합니다.')
        
        node = Node(key, data)
        index = self.hash(node)
        
        if (self.table[index] is None):
            self.table[index] = node
        else:
            link = self.table[index] # 해당 인덱스에 저장된 첫번재 노드
            
            while(True):
                if link == node: # 만약 link의 key값과 node의 key값이 같다면 데이터를 추가하지 않고 return
                    link.data = node.data
                    return
                
                if link.next is None:
                    link.next = node
                    break
                
                link = link.next
                
        self.length += 1
        '''
        self.__add_data(key, data, self.__set)
        
        
    def get(self, key: str):
        if type(key) is not str:
            raise TypeError('Key는 str타입입니다.')
        
        index = self.hash(Node(key, -1))
        link = self.table[index]
        
        while(link is not None):
            if link.key == key:
                return link.data
            
            link = link.next
        return None # link를 모두 탐색했지만 key가 일치하는 것이 없다면 data가 없기때문에 None으로 리턴한다.
    
    
    # 모든 데이터를 탐색할 수 있게 하자
    # 포인터를 이동시켜 index를 확인
    def __contains__(self, key):
        return True if self.get(key) is not None else False
    
    
    def __iter__(self):
        return HashTable.Iterator(self)
        
    class Iterator:
        def __init__(self, hashtable):
            self.hashtable = hashtable
            self.index = 0
            self.link = None
            
            while self.index < self.hashtable.max_len:
                if self.hashtable.table[self.index] is not None:
                    self.link = self.hashtable.table[self.index]
                    break
                self.index += 1
            
        def __iter__(self):
            return self
        
        # next는 Node를 반환하도록 구현
        def __next__(self):
            if self.link is None:
                raise StopIteration
            
            current_link = self.link
            self.link = self.link.next
            
            if self.link is None:
                self.index += 1
                while self.index < self.hashtable.max_len:
                    if self.hashtable.table[self.index] is not None:
                        self.link = self.hashtable.table[self.index]
                        break
                    self.index += 1
                    
            return current_link