# [01] 그리디 - 거스름돈


# 1. 1260원
n = 1260
count = 0

# 2. 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

# 3. 동전세기
for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

# 4. 동전 개수 출력
print(count)