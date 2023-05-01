'''Lv.1 수박수박수박수박수박수?'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12922


# 풀이 1
def solution(n):
    answer = "수박" * (n // 2) + "수" * (n % 2)
    return answer