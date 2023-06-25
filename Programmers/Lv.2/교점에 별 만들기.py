'''Lv.2 교점에 별 만들기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/87377


# 풀이 1
from itertools import combinations

def solution(line):
    dots = []
    answer = []
    
    # 1. 정수 교점 구하기
    for (A, B, E), (C, D, F) in combinations(line, 2):
        if A*D-B*C == 0:
            continue
        else:
            x = (B*F-E*D) / (A*D-B*C)
            y = (E*C-A*F) / (A*D-B*C)
            if x==int(x) and y==int(y) and (int(x), int(y)) not in dots:
                dots.append((int(x), int(y)))
    #print(dots)
    
    # 2. 격자판 범위 구하기
    x_list = [x for (x, y) in dots]
    y_list = [y for (x, y) in dots]
    x_min, x_max = min(x_list), max(x_list)
    y_min, y_max = min(y_list), max(y_list)
    #print(x_min, x_max, y_min, y_max)
    
    # 3. 별 그리기
    for yi in range(y_max, y_min-1, -1):
        ans = ""
        for xi in range(x_min, x_max+1):
            if (xi, yi) in dots:
                ans += '*'
            else:
                ans += '.'
        answer.append(ans)
        #print(ans)
        
    return answer


# 풀이 2
from itertools import combinations

def solution(line):
    INF = int(1e12)
    dots = set()
    x_min, x_max, y_min, y_max = INF, -INF, INF, -INF
    answer = []
    
    # 1. 정수 교점 구하기
    for (A, B, E), (C, D, F) in combinations(line, 2):
        if A*D-B*C == 0:
            continue
        else:
            x = (B*F-E*D) / (A*D-B*C)
            y = (E*C-A*F) / (A*D-B*C)
            if x==int(x) and y==int(y):
                x, y = int(x), int(y)
                dots.add((x, y))
                # 2. 격자판 범위 구하기
                x_min, x_max = min(x_min, x), max(x_max, x)
                y_min, y_max = min(y_min, y), max(y_max, y)
    
    # 3. 별 그리기
    for yi in range(y_max, y_min-1, -1):
        ans = ""
        for xi in range(x_min, x_max+1):
            if (xi, yi) in dots:
                ans += '*'
            else:
                ans += '.'
        answer.append(ans)
        
    return answer