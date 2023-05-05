'''Lv.1 내적'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/70128


# 풀이 1
def solution(a, b):
    return sum(a * b for a, b in zip(a, b))


# 풀이 2
def solution2(a, b):
    answer = []
    for a, b in zip(a, b):
        answer.append(a * b)
    return sum(answer)


# 풀이 3
def solution3(a, b):
    answer = []
    for i in range(len(a)):
        answer.append(a[i] * b[i])
    return sum(answer)


# 풀이 4
def solution4(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer