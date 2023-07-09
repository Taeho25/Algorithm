'''Lv.2 [1차] 프렌즈4블록'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/17679


# 풀이 1
def solution(m, n, board):
    answer = 0
    
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        print(board)
        # 1. 4블록 세트 좌표 기록
        rm = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == ' ':
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    rm.add((i, j))
                    rm.add((i+1, j))
                    rm.add((i, j+1))
                    rm.add((i+1, j+1))
        
        # 2. 지울 좌표가 있다면 지우기, 없다면 결과 반환 
        if rm:
            answer += len(rm)
            for (i, j) in rm:
                board[i][j] = ' '
        else:
            return answer
        
        # 3. 블록을 아래로 드랍
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] != ' ' and board[i+1][j] == ' ':
                        board[i+1][j] = board[i][j]
                        board[i][j] = ' '
                        moved = 1
            if moved == 0:
                break
