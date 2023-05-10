# [29] 다이나믹 프로그래밍 - 바닥 공사


# 1. 정수 N 입력 / dp 테이블 초기화
n = int(input())
d = [0] * 1001

# 2. 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

# 3. 결과 출력
print(d[n])