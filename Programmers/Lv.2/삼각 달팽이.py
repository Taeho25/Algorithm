'''Lv.2 삼각 달팽이'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/68645


# 풀이 1
def solution(n):
    ans = [[0]*i for i in range(1, n+1)]
    dcol = [1, 0, -1]  # down, right, left-up
    drow = [0, 1, -1]
    
    number = n * (n+1) // 2
    col, row = 0, 0
    d = 0
    for num in range(1, number+1):
        # 1. 숫자 채우기, 다음 좌표 구하기
        ans[col][row] = num
        ncol = col + dcol[d]
        nrow = row + drow[d]
        # 2. 다음 좌표 수정 필요성 확인
        if ncol >= n or nrow >= n or ans[ncol][nrow] != 0:
            d = (d + 1) % 3
            ncol = col + dcol[d]
            nrow = row + drow[d]
        # 3. 적용
        col, row = ncol, nrow
    # 4. 리스트 정리
    answer = []
    for l in ans:
        answer += l

    return answer


# 풀이 2 : 4번 과정 구현만 변경
def solution(n):
    ans = [[0]*i for i in range(1, n+1)]
    dcol = [1, 0, -1]  # down, right, left-up
    drow = [0, 1, -1]
    
    number = n * (n+1) // 2
    col, row = 0, 0
    d = 0
    for num in range(1, number+1):
        # 1. 숫자 채우기, 다음 좌표 구하기
        ans[col][row] = num
        ncol = col + dcol[d]
        nrow = row + drow[d]
        # 2. 다음 좌표 수정 필요성 확인
        if ncol >= n or nrow >= n or ans[ncol][nrow] != 0:
            d = (d + 1) % 3
            ncol = col + dcol[d]
            nrow = row + drow[d]
        # 3. 적용
        col, row = ncol, nrow
    # 4. 리스트 정리
    answer = sum(ans, [])

    return answer

