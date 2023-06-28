'''Lv.2 빛의 경로 사이클'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/86052


# 풀이 1
def solution(grid):
    answer = []
    visited = [[[False]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # down, left, up, right
    handle = {'S':0, 'L':-1, 'R':1}
    
    # 격자 좌표, 방향 선택
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            for d in range(4):
                if visited[col][row][d]:
                    continue
                cnt = 0
                n_col, n_row = col, row
                
                #print(f"start point: ({n_col}, {n_row}, {d})")
                while not visited[n_col][n_row][d]:
                    # 1. 현위치, 방향 방문처리
                    visited[n_col][n_row][d] = True # 방문처리
                    cnt += 1
                    #print(f"{cnt} : ({n_col}, {n_row}, {d})")

                    # 2. 다음 위치, 방향 계산
                    n_col = (n_col + direction[d][0]) % len(grid)
                    n_row = (n_row + direction[d][1]) % len(grid[0])
                    c = grid[n_col][n_row]
                    d = (d + handle[c]) % 4
                
                answer.append(cnt)
                #print("Cycle Length:", cnt)
                #print()
    answer.sort()
    
    return answer


# 풀이 2
def solution(grid):
    answer = []
    visited = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dcol = (1, 0, -1, 0)
    drow = (0, -1, 0, 1)  
 
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            for d in range(4):
                if visited[col][row][d]:
                    continue
                cnt = 0
                n_col, n_row = col, row
                
                while not visited[n_col][n_row][d]:
                    visited[n_col][n_row][d] = True
                    cnt += 1
                    if grid[n_col][n_row] == "S":
                        pass
                    elif grid[n_col][n_row] == "L":
                        d = (d - 1) % 4
                    elif grid[n_col][n_row] == "R":
                        d = (d + 1) % 4
                    
                    n_col = (n_col + dcol[d]) % len(grid) 
                    n_row = (n_row + drow[d]) % len(grid[0])
 
                answer.append(cnt)
    answer.sort()

    return answer