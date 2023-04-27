# [03] 그리디 - 숫자 카드 게임


# 1. N, M 입력
n, m = map(int, input().split())

# 2-1. 알고리즘
if False:
    result = 0
    for i in range(n):                           # 한 줄씩 입력받아 확인
        data = list(map(int, input().split()))     
        min_value = min(data)                        # 현재 줄에서 '가장 작은 수' 찾기
        result = max(result, min_value)              # '가장 작은 수'들 중에서 가장 큰 수 찾기
# 2-2. 알고리즘
if True:
    result = 0
    for i in range(n):
        data = list(map(int, input().split()))
        min_value = 10001
        for a in data:
            min_value = min(min_value, a)
        result = max(result, min_value)

# 3. 결과 출력
print(result)