# [22] 이진 탐색 - 반복문 구현

# 이진 탐색의 전제 조건은 데이터 정렬


# 1. 이진 탐색 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 2. N(원소의 개수), target(찾고자 하는 문자열) / array(전체 원소) 입력
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 3. 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)