'''Lv.1 두 개 뽑아서 더하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/68644


# 풀이 1
def solution(numbers):
    answer = []
    for idx1 in range(0, len(numbers)-1):
        for idx2 in range(idx1+1, len(numbers)):
            number = numbers[idx1] + numbers[idx2]
            if number not in answer:
                answer.append(number)
    answer.sort()
    return answer


# 풀이 2
def solution(numbers):
    answer = set()
    for idx1 in range(0, len(numbers)-1):
        for idx2 in range(idx1+1, len(numbers)):
            answer.add(numbers[idx1] + numbers[idx2])
    return sorted(list(answer))


# 풀이 3
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


# 풀이 4
from itertools import combinations
def solution(numbers):
    answer = []
    number_set = list(combinations(numbers, 2))
    for n1, n2 in number_set:
        answer.append(n1 + n2)
    answer = list(set(answer))
    return sorted(answer)