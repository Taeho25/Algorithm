'''Lv.2 피보나치 수'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12945


# 풀이 1
def solution(n):
    f = [0]*100001
    f[0], f[1] = 0, 1
    
    for num in range(2, n+1):
        f[num] = f[num-1] + f[num-2]
    
    return f[n] % 1234567


# 풀이 2
def solution(n):
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a + b
        
    return a % 1234567