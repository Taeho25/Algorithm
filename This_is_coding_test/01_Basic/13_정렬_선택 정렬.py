# [13] 정렬 - 선택 정렬

# 비교 기반의 정렬 알고리즘
# 가장 작은 것을 선택하여 정렬한다.
# O(N^2)


# 1. 데이터
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 2. 선택 정렬
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

# 3. 결과 출력
print(array)