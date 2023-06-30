'''Lv.2 거리두기 확인하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/81302


# 풀이 1
from collections import deque

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def bfs(place, x, y):
    # 1. 초기화
    visited = [[False]*5 for _ in range(5)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True
    
    # 2. queue에 노드가 있는 동안 bfs 수행
    while queue:
        x, y, cost = queue.popleft()
        if cost == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]: continue
                if place[nx][ny] == 'P':
                    return False
                elif place[nx][ny] == 'O':
                    queue.append((nx, ny, cost + 1))
                    visited[nx][ny] = True
    
    return True

def solution(places):
    answer = []

    for place in places:
        p = [list(place[i]) for i in range(5)]
        good = 1
        
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P' and good:
                    if not bfs(p, i, j):
                        good = 0
            if not good: break
            
        answer.append(good)

    return answer