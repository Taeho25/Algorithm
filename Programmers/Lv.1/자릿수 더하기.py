'''Lv.1 자릿수 더하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12931


# 풀이 1
def solution(n):
    ns = list(map(int, str(n)))
    return sum(ns)