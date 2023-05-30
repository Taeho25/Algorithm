'''Lv.0 안전지대'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120866


# 풀이 1
def solution(board):
    answer = 0
    d = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (board[x][y] == 1):
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if (nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0])):
                        if board[nx][ny] != 1:
                            board[nx][ny] = 2
    
    print(board)
    
    answer = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                answer += 1
    
    return answer