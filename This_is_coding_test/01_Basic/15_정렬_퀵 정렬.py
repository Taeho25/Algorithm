# [15] 정렬 - 퀵 정렬

# 비교 기반의 정렬 알고리즘
# 기준 데이터를 설정하고, 그것보다 큰 데이터와 작은 데이터의 위치를 바꿔 정렬한다.
# 데이터가 이미 정렬되어 있는 경우에는 매우 느리게 동작한다. 최악의 경우 O(N^2)
# 최악의 경우를 방지하기 위해 피벗값 설정 로직이 추가로 존재한다.
# O(NlogN)


# 1. 데이터
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 2. 퀵 정렬 함수 정의
def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우에도 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# 3. 퀵정렬 시행
quick_sort(array, 0, len(array)-1)

# 4. 결과 출력
print(array)