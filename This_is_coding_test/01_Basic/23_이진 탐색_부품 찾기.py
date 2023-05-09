# [23] 이진 탐색 - 부품 찾기


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

# 2. N(부품 개수) / array(전체 부품) / M(확인 요청 부품 개수) / x(확인 요청 부품) 입력
n = int(input())
array = list(map(int, input().split()))
array.sort()    # 정렬 
m = int(input())
x = list(map(int, input().split()))

# 3. 확인 요청 부품 번호 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('No', end=' ')