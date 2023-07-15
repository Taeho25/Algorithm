'''Lv.2 거리두기 확인하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/81302


# 풀이 1
def solution(places):
    answer = []
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    places_list = [[list(p) for p in place] for place in places]
    
    # place 하나씩 확인
    for place in places_list:
        good = 1
        
        # place 내 5x5 공간 하나씩 확인
        for x in range(5):
            if good == 0: break
            for y in range(5):
                if good == 0: break
                if place[x][y] != 'P': continue
                
                # 1. (x,y) 기준 방문처리 리셋
                visited = [[False]*5 for _ in range(5)]
                visited[x][y] = True
                
                # 2. Step 1
                for i in range(4):
                    if good == 0: break
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (0 <= nx < 5) and (0 <= ny < 5) and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        if place[nx][ny] == 'P':  # 사람이 있으면 거리두기 X
                            good = 0
                            break
                        elif place[nx][ny] == 'X':  # 파티션 있으면 거리두기 O (더 안 봐도 됨)
                            continue
                        
                        # 3. Step 2 (이전이 빈테이블인 경우만 한 번 더 가보기)
                        for i2 in range(4):
                            nx2 = nx + dx[i2]
                            ny2 = ny + dy[i2]
                            if (0 <= nx2 < 5) and (0 <= ny2 < 5) and visited[nx2][ny2] == False:
                                visited[nx2][ny2] = True
                                if place[nx2][ny2] == 'P':  # step1: 빈테이블 / step2: 사람 -> 거리두기 X
                                    good = 0
                                    break
        
        answer.append(good) 
    
    return answer


# 풀이 2
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
