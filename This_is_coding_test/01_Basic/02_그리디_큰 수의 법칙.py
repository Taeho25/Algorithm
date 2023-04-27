# [02] 그리디 - 큰수의 법칙


# 1. N, M, K 입력 / N개의 수 입력
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 2. 입력 데이터 정렬 / 1st, 2nd 수 찾기
data.sort()
first = data[n-1]
second = data[n-2]

# 3-1. 알고리즘
if False:
    result = 0
    while True:
        for i in range(k):    # 1st 수를 K번 더하기
            if m == 0: break      # m이 0이라면 탈출
            result += first
            m -= 1                # 결과에 first를 더할 때 마다 m에서 1씩 빼기
        
        if m == 0: break      # m이 0이면 무한루프 탈출

        result += second      # 2nd 수를 한 번 더하기
        m -= 1                # 결과에 second를 더할 때 마다 m에서 1씩 빼기
# 3-2. 알고리즘(V)
if True:
    count = int(m / (k + 1)) * k   # 1st 수가 더해지는 횟수 계산
    count += m % (k + 1)

    result = 0
    result += (count) * first      # 1st 수 count번 더하기
    result += (m - count) * second # second 수 더하기


# 4. 결과 출력
print(result)