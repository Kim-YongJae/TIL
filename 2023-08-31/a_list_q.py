# 1. 자연수 배열에서 가장 큰 수 찾기
def check_max(arr):
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max


# 2. 자연수 배열에서 가장 큰 두 수를 찾아 배열로 반환
def check_max2(arr):
    if len(arr)<2: return arr
    
    max,second=arr[:2]
    
    if max<second:
        max,second=second,max
    for e in arr[2:]:
        if e>max:
            max,second=e,max
        elif e>second:
            second=e
    return [max,second]

# 3. 앞으로 읽어도, 뒤로 읽어도 같은 단어(회문)인지 검사하는 함수를 작성
# aabaa -> True
# aaabaa -> False
# hint: 문자열도 배열이다. 기러기, 토마토, 역삼역

'''
def check_palindrome(text):
    if text==text[::-1]:
        return True
    else:
        return False
'''
'''강사님 풀이
def check_palindrome(text):
    left, right = 0, len(text)-1
    
    while(left<right):
        if text[left] != text[right]:
            return False
            
        left, right = left+1, right-1
        
    return True
'''

def check_palindrome(text):
    for i in range(len(text)//2):
        if text[i] == text[len(text)-i-1]:
            return True
        else:
            False