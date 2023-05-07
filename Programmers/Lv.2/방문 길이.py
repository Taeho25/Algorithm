'''Lv.2 방문 길이'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/49994


# 풀이 1
def solution(dirs):
    dx = {'U':0, 'D':0, 'R':1, 'L':-1}
    dy = {'U':1, 'D':-1, 'R':0, 'L':0}
    x, y = 0, 0
    path = []
    
    for dir in dirs:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
            
        if [x, y, nx, ny] not in path:
            path.append([x, y, nx, ny])
            path.append([nx, ny, x, y])
        x, y = nx, ny

    return len(path) // 2


# 풀이 2
def solution(dirs):
    d = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    x, y = 0, 0
    path = set()
    
    for dir in dirs:
        nx = x + d[dir][0]
        ny = y + d[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path.add((x, y, nx, ny))
            path.add((nx, ny, x, y))
            x, y = nx, ny

    return len(path) // 2