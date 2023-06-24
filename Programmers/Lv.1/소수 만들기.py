'''Lv.1 소수 만들기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12977


# 풀이 1
from itertools import combinations

def isPrime(num):
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for num3 in combinations(nums, 3):
        if isPrime(sum(num3)):
            answer += 1    

    return answer