# [20] 정렬 - 두 배열의 원소 교체


# 1. N, K 입력 / 배열 A, B 입력
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 2. A, B 정렬
a.sort()
b.sort(reverse=True)

# 3. 비교, 교환
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

# 4. 결과 출력
print(sum(a))