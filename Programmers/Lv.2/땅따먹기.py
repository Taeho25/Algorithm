'''Lv.2 땅따먹기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12913


# 풀이 1
def solution(land):

    for row in range(1,len(land)):
        for col in range(4):
            pre_scores = land[row-1][:col] + land[row-1][col+1:]
            land[row][col] += max(pre_scores)

    return max(land[-1])
