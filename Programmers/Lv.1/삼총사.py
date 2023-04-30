'''Lv.1 삼총사'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/131705


# 풀이 1
def solution(number):
    answer = 0
    for idx1 in range(len(number)-2):
        for idx2 in range(idx1+1, len(number)-1):
            for idx3 in range(idx2+1, len(number)):
                if number[idx1] + number[idx2] + number[idx3] == 0:
                    answer += 1
    return answer


# 풀이 2
def solution2 (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number, 3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt