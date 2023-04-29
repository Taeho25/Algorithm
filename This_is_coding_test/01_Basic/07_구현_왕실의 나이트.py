# [07] 구현 - 왕실의 나이트


# 1. 현재 나이트 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 2. 나이트 이동 가능 방향 정의
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

# 3. 알고리즘
result = 0
for step in steps:    # 8가지 방향 확인
    next_row = row + step[0]    # 이동 후 위치 확인
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:    # 이동가능하면 카운트 +1
        result += 1

# 4. 결과 출력
print(result)