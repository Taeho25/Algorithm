'''Lv.2 N개의 최소공배수'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12953


# 풀이 1
from fractions import gcd

def solution(arr):      
    answer = 1

    for num in arr:
        answer = (num * answer) / gcd(num, answer)

    return answer


# 풀이 2
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def solution(arr):
    answer = 1

    for num in arr:
        answer = (num * answer) / gcd(num, answer)
    
    return answer