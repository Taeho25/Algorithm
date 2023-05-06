'''Lv.2 짝지어 제거하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12973


# 풀이 1
def solution(s):
    stack = []
    
    for alpha in s:
        if len(stack) == 0 or alpha != stack[-1]:
            stack.append(alpha)
        else:
            stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0 