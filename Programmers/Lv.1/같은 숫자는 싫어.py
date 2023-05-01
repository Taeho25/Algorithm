'''Lv.1 같은 숫자는 싫어'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12906


# 풀이 1
def solution(arr):
    answer = []
    last_num = -1
    for number in arr:
        if number != last_num:
            answer.append(number)
            last_num = number
    return answer


# 풀이 2
def solution2(arr):
    answer = []
    for num in arr:
        if answer[-1:] == [num]: continue
        answer.append(num)
    return answer