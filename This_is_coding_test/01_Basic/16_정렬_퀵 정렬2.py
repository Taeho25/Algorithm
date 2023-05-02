# [16] 정렬 - 퀵 정렬2

# 비교 기반의 정렬 알고리즘
# 기준 데이터를 설정하고, 그것보다 큰 데이터와 작은 데이터의 위치를 바꿔 정렬한다.
# 데이터가 이미 정렬되어 있는 경우에는 매우 느리게 동작한다. 최악의 경우 O(N^2)
# 최악의 경우를 방지하기 위해 피벗값 설정 로직이 추가로 존재한다.
# O(NlogN)


# 1. 데이터
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 2. 퀵 정렬 함수 정의
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분
    #print(pivot, "L:", left_side, "/ R:", right_side)

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# 3. 퀵정렬 시행 및 결과 출력
print(quick_sort(array))