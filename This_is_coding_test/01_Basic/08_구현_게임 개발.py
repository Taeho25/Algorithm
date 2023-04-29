# [08] 구현 - 게임 개발


# 1. N, M 입력 / 현재 캐릭터 X, Y 좌표, 방향 입력
n, m = map(int, input().split())
x, y, direction = map(int, input().split())


# 2. 방문 위치 저장 맵 생성, 0으로 초기화 / 현재 위치 방문처리
d = [[0] * m for _ in range(n)]    # 리스트 컴프리헨션
d[x][y] = 1

# 3. 맵 정보 입력 / 북, 동, 남, 서 정의 / 왼쪽 회전 함수 정의
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 4. 알고리즘 (시뮬레이션)
def turn_left():
    global direction
    direction -= 1
    if direction == -1: direction = 3

count = 1
turn_time = 0
while True:
    # (1) 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # (2) 안 가본 칸, 땅? : 이동 or 회전 횟수 +1
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    # (3) 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:    # 뒤로 갈 수 있다면 이동
            x = nx
            y = ny
        else:    # 못 가면(바다면) 무한루프 종료
            break
        turn_time = 0

# 5. 결과 출력
print(count)