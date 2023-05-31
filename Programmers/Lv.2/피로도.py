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
