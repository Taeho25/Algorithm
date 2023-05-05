'''Lv.1 없는 숫자 더하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/86051


# 풀이 1
def solution(numbers):
    return sum(range(10)) - sum(numbers)


# 풀이 2
def solution2(numbers):
    answer = 0
    for n in range(1, 10):
        if n not in numbers:
            answer += n
    return answer


# 풀이 3
def solution3(numbers):
    return sum(set(range(10)) - set(numbers))


# 풀이 4
def solution(numbers):
    return sum([i for i in range(10) if i not in numbers])