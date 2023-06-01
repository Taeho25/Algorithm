'''Lv.0 연속된 수의 합'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120923


# 풀이 1
def solution(num, total):
    sum_steps = (num - 1) * num // 2  # 0 ~ num-1 의 합
    start = (total - sum_steps) // num
    answer = [n for n in range(start, start + num)]
    
    return answer


# 풀이 2
def solution(num, total):
    sum_steps = sum(range(num))  # 0 ~ num-1 의 합
    start = (total - sum_steps) // num
    answer = [n for n in range(start, start + num)]
    
    return answer