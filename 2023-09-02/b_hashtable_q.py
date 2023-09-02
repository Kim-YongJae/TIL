from b_hashtable import *

# 주어진 문자열에서 가장 많이 반복되는 문자를 찾아 배열에 담아 반환하는 함수를 작성
def find_uniq_char(text):
    cnt={}
    
    for char in text:
        if char in cnt:
            cnt[char] += 1
        else:
            cnt[char] = 1
            
    max_cnt = max(cnt.values())
    most_char = [char for char, count in cnt.items() if count == max_cnt]
    
    return most_char

def find_uniq_char1(text):
    hashtable = HashTable()
    
    for char in text:
        if char in hashtable:
            hashtable.set(char, hashtable.get(char) + 1)
        else:
            hashtable.add(char, 1)
            
    max_cnt = max([node.data for node in hashtable])
    most_char = [node.key for node in hashtable if node.data == max_cnt]
    
    return most_char

'''
def find_uniq_char(text):
    hashtable = HashTable()
    
    for ch in text:
        if ch in hashtable:
            cnt = hashtable.get(ch)
            hashtable.set(ch, cnt+1)
        else:
            hashtable.add(ch, 1)
            
    res = []
    max = 1
   
    for e in hashtable:
        if max < e.data:
            max = e.data
    for e in hashtable:
        if max == e.data:
            res.append(e.key)
    
    return res
'''