# [18] 정렬 - 위에서 아래로


# 1. N 입력 / N개 정수 입력 및 리스트에 저장
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

# 2. 정렬
array = sorted(array, reverse=True)

# 3. 결과 출력
for i in array:
    print(i, end=' ')
