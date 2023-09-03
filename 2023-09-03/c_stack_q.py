from c_stack import *
from b_hashtable import *

# (), {}, [] 세 가지 괄호가 알맞게 열리고 닫혔는지 판단하는 is_pair 함수를 작성하시오

def is_pair(text):
    stack = Stack()
    ga = {')': '(', '}': '{', ']': '['}

    for char in text:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != ga[char]:
                return False
                
    return stack.is_empty()

    
'''해시태그 사용 안함
def is_pair(text):
    stack = Stack()
    for ch in text:
        if ch =='(' or ch == '{' or ch == '[':
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
                open = stack.pop()
            if open == '(':
                if ch != ')':
                    return False
            if open == '{':
                if ch != '}':
                    return False
            if open == '[':
                if ch != ']':
                    return False
    return True if stack.is_empty() else False
'''
'''
def is_pair(text):
    hashtable = HashTable()
    hashtable.add('(',')')
    hashtable.add('[',']')
    hashtable.add('{','}')
    
    stack = Stack()
    
    for ch in text:
        if ch in hashtable:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
                
            k=stack.pop()
            
            if ch != hashtable.get(k):
                return False
                
    return True if stack.is_empty() else False
'''

''' 해시태그를 이해하기 위한 간단한 예시문
def hello():
    print('안녕')
    
def bye():
    print('잘가')
    
def study():
    print('공부')

dict = {'hello':hello, 'bye':bye, 'study':study}

def translate_eng_to_kor(eng):
    dict[eng]()

translate_eng_to_kor('hello')
translate_eng_to_kor('bye')
translate_eng_to_kor('study')
'''
    

print(is_pair('{}()[]')) # True
print(is_pair('{([])}')) # True
print(is_pair('{([}])}')) # False
print(is_pair('{([])}{{}')) # False