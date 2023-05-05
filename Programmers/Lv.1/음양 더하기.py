'''Lv.1 음양 더하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/76501


# 풀이 1
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]: answer += absolutes[i]
        else: answer += absolutes[i] * (-1)
    return answer


# 풀이 2
def solution2(absolutes, signs):
    answer = []
    for absolute, sign in zip(absolutes, signs):
        if sign: answer.append(absolute)
        else: answer.append(-absolute)
    return sum(answer)


# 풀이 3
def solution3(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))