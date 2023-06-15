'''Lv.0 길이에 따른 연산'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181879


# 풀이 1
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        answer = 1
        for n in num_list:
            answer *= n
        return answer


# 풀이 2
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))
    

# 풀이 3
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)