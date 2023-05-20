'''Lv.2 다음 큰 숫자'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12911


# 풀이 1
def solution(n):
    n1_1 = bin(n)[2:].count('1')
    
    while(True):
        n += 1
        n2_1 = bin(n)[2:].count('1')
        if n1_1 == n2_1: return n