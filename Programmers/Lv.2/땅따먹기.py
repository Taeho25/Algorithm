'''Lv.2 땅따먹기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12913


# 풀이 1
def solution(land):

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[len(land)-1])