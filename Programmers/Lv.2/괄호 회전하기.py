'''Lv.2 괄호 회전하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/76502


# 풀이 1
from collections import deque

def solution(s):
    answer = 0
    
    for t in range(len(s)):
        # 1. 괄호 회전
        queue = deque(s)
        for _ in range(t):
            front = queue.popleft()
            queue.append(front)
        #print(queue)
        
        # 2. 괄호 확인
        stack = []
        cnt = 0
        for ch in queue:
            if ch == '[' or ch == '(' or ch == '{':
                stack.append(ch)
            elif len(stack) == 0:
                break
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            else:
                break
            cnt += 1
            
        if cnt == len(queue) and len(stack) == 0:
            answer += 1
            
    return answer


# 풀이 2
def solution(s):
    answer = 0
    
    for t in range(len(s)):
        queue = s[t:]+s[:t]
        
        stack = []
        for ch in queue:
            if len(stack) == 0:
                stack.append(ch)
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(ch)
            
        if len(stack) == 0:
            answer += 1
            
    return answer


# 풀이 3
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif ch == ')' and stack[-1] == '(':
            stack.pop()
        elif ch == '}' and stack[-1] == '{':
            stack.pop()
        elif ch == ']' and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(ch)

    return False if stack else True

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer


# 풀이 4
from collections import deque

def check(s):
    while True:
        if "()" in s:
            s = s.replace("()","")
        elif "{}" in s:
            s = s.replace("{}","")
        elif "[]" in s:
            s = s.replace("[]","")
        else:
            return False if s else True       

def solution(s):
    answer = 0
    que = deque(s)

    for i in range(len(s)):
        if check(''.join(que)): answer += 1
        que.rotate(-1)
    return answer
