'''Lv.0 겹치는 선분의 길이'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120876


# 풀이 1
def solution(lines):
    answer = 0
    line = [0]*201
    for [start, end] in lines:
        for spot in range(start, end):
            line[spot+100] += 1
    
    answer = 0
    for l in line:
        if l >= 2:
            answer += 1
            
    return answer


# 풀이 2
def solution(lines):
    sets = []
    for start, end in lines:
        temp = set(range(start, end))
        sets.append(temp)
    #print(sets)

    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


# 풀이 3
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])