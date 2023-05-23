'''Lv.0 정수를 나선형으로 배치하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181832


# 풀이 1
def solution(n):
    answer = [[0]*n for i in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0] # right -> down -> left -> up -> right ...
    x, y = 0, 0
    
    now = 0
    for number in range(1, n**2 + 1):
        #print((x, y), number)
        answer[x][y] = number
        
        nx = x + dx[now]
        ny = y + dy[now]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            now = (now + 1) % 4
            nx = x + dx[now]
            ny = y + dy[now]
        
        x, y = nx, ny
    
    return answer


# 풀이 2
def solution(n):
    answer = [[0]*n for i in range(n)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    now = 0

    for number in range(1, n**2 + 1):
        answer[x][y] = number
        
        nx, ny = x + d[now][0], y + d[now][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            now = (now + 1) % 4
            nx, ny = x + d[now][0], y + d[now][1]
        
        x, y = nx, ny
    
    return answer
