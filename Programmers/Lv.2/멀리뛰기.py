'''Lv.2 멀리뛰기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12914


# 풀이 1
def solution(n):
    step = [0]*2001
    step[1] = 1
    step[2] = 2
    
    for i in range(3, n+1):
        step[i] = step[i-1] + step[i-2] 
    
    return step[n] % 1234567


# 풀이 2
def solution(n):
    a, b = 1, 2
    
    for _ in range(n-1):
        a, b = b, a + b 
    
    return a % 1234567
