# [28] 다이나믹 프로그래밍 - 개미전사


# 1. 정수 N 입력 / 식량 정보 array 입력 / DP 테이블 초기화
n = int(input())
array = list(map(int, input().split()))
d = [0] * 100

# 2. 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 3. 결과 출력
print(d[n-1])
for i in range(n):
    print(d[i], end=" ")