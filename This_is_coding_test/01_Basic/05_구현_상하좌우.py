# [05] 구현 - 상하좌우


# 1. N 입력 / 좌표 초기화 / 이동 계획 입력
n = int(input())
x, y = 1, 1
plans = input().split()

# 2. L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 3. 알고리즘
for plan in plans:    # 이동 계획 하나씩 확인
  for i in range(len(move_types)):    # 이동 방향에 따른 다음 좌표 계산
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n: continue    # 공간을 벗어나면 무시
  x, y = nx, ny    # 이동 수행

# 4. 결과 출력
print(x, y)