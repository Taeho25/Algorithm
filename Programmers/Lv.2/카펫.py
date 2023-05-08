'''Lv.2 카펫'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42842


# 풀이 1
def solution(brown, yellow):
    divisor = []
    finish = int(yellow**0.5)
    
    for num in range(1, finish+1):
        if yellow % num == 0:
            divisor.append((yellow//num, num))
    
    for w, h in divisor:
        if brown == (w + h) * 2 + 4:
            return [w+2, h+2]
                

# 풀이 2
def solution(brown, yellow):
    for num in range(1, int(yellow**0.5) + 1):
        if yellow % num == 0:
            if brown == (num + yellow//num) * 2 + 4:
                return [yellow//num+2, num+2]


# 풀이 3
def solution(brown, yellow):
    for num in range(1, int(yellow**0.5) + 1):
        if yellow % num == 0 and brown == (num + yellow//num) * 2 + 4:
            return [yellow//num+2, num+2]
        

# 풀이 4
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2 - 4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2 - 4*(brown+yellow)))/2
    return [w, h]