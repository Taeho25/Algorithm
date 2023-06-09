# [27] 다이나믹 프로그래밍 - 1로 만들기


# 1. 정수 X 입력 / DP 테이블 초기화
X = int(input())
d = [0] * 30001

# 2. 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, X + 1):
    # 현재의 수에서 1을 뺴는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if X % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if X % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if X % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[X])