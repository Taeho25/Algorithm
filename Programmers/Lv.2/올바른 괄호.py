'''Lv.2 올바른 괄호'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12909


# 풀이 1
def solution(s):
    stack = []
    
    for word in s:
        if word == '(':
            stack.append(word)
        else:
            if len(stack) == 0 or stack[-1] != '(': return False
            else: stack.pop()
    
    return True if len(stack) == 0 else False


# 풀이 2
def solution(s):
    pair = 0

    for word in s:
        if pair < 0: break
        pair = pair + 1 if word == "(" else pair - 1 if word == ")" else pair
        
    return pair == 0