'''Lv.1 약수의 개수와 덧셈'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/77884


# 풀이 1
def solution(left, right):    
    answer = 0
    for n in range(left, right+1):
        if int(n**0.5) != n**0.5:  # 약수 짝수개
            answer += n
        else:  # 약수 홀수개
            answer -= n
    return answer


# 풀이 2
import math
def solution2(left, right):    
    answer = 0
    for n in range(left, right+1):
        if int(math.sqrt(n)) != math.sqrt(n):  # 약수 짝수개
            answer += n
        else:  # 약수 홀수개
            answer -= n
    return answer


# 풀이 3
def solution3(left, right):
    return sum(n if (n ** 0.5) % 1 else -n for n in range(left, right + 1))