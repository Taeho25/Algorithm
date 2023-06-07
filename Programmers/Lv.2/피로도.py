'''Lv.2 피로도'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/87946


# 풀이 1
from itertools import permutations

def solution(k, dungeons):
    steps = []
    
    for scenario in permutations(dungeons, len(dungeons)):
        #print(scenario)
        stemina = k
        step = 0
        for dungeon in scenario:
            if stemina >= dungeon[0]:
                stemina -= dungeon[1]
                step += 1
            else:
                break     
        steps.append(step)
                
    return max(steps)


# 풀이 2
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
