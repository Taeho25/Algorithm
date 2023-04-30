'''Lv.1 문자열 내 마음대로 정렬하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12915


# 풀이 1
def solution(strings, n):
    answer = sorted(strings, key = lambda x: (x[n], x))
    return answer


# 풀이 2
def solution2(strings, n):
    strings.sort()
    answer = sorted(strings, key = lambda x: x[n])
    return answer