# [04] 그리디 - 1이 될 때까지


# 1. N, K 입력 / 결과 초기화
n, k = map(int, input().split())
result = 0

# 2-1. 알고리즘
if False:
    while n >= k:           # N이 K 이상이라면 K로 계속 나누기
        while n % k != 0:       # 나누어 떨어지지 않는다면
            n -= 1              # N에서 1씩 빼기
            result += 1
        n //= k                 # K로 나누기
        result += 1
    while n > 1:            # 마지막으로 남은 수에 대하여 1씩 빼기
        n -= 1
        result += 1
# 2-2. 알고리즘
if True:
    while True:
        target = (n // k) * k   # N이 K로 나누어 떨어질 때 까지 1씩 빼기
        result += (n - target)
        n = target              
        if n < k: break         # N을 K로 더 이상 나눌 수 없을 때 무한루프 탈출
        n //= k                 # N을 K로 나누기
        result += 1
    result += (n - 1)

# 3. 결과 출력
print(result)