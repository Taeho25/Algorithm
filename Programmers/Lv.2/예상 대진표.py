'''Lv.2 예상 대진표'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12985


# 풀이 1
def solution(n,a,b):
    answer = 0
    if a > b:
        a, b = b, a
    
    while(1):
        answer += 1
        if b % 2 == 0 and a == b - 1:
            return answer
        a = a // 2 + a % 2
        b = b // 2 + b % 2