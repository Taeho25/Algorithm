'''Lv.1 문자열 내림차순으로 배치하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12917


# 풀이 1
def solution(s):
    answer = sorted(s, reverse=True)
    return "".join(answer)