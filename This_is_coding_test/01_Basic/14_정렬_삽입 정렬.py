# [14] 정렬 - 삽입 정렬

# 비교 기반의 정렬 알고리즘
# 특정 데이터를 적절한 위치에 삽입히여 정렬한다.
# 데이터가 이미 어느정도 정렬되어 있는 경우에 매우 빠르게 동작한다.
# O(N^2)


# 1. 데이터
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 2. 삽입 정렬
for i in range(len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

# 3. 결과 출력
print(array)