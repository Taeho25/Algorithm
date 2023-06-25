'''Lv.2 멀쩡한 사각형'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/62048


# 풀이 1
def solution(w,h):
    for gcd in range(min(w,h), 0, -1):
        if (w % gcd == 0) and (h % gcd == 0):
            return w*h - (w + h - gcd)
        

# 풀이 2
def gcd(a, b):
    if a==0:
        return b
    else:
        return gcd(b%a, a)

def solution(w, h):
    return w*h - (w + h - gcd(w, h))


# 풀이 3
from math import gcd

def solution(w, h):
    return w*h - (w + h - gcd(w, h))
