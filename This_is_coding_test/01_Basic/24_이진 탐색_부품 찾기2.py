# [24] 이진 탐색 - 부품 찾기 by 계수 정렬


# 1. N입력 / array 초기화 / 전체 부품 / 확인 요청 부품 개수 / 확인 요청 부품 입력
n = int(input())
array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1
m = int(input())
x = list(map(int, input().split()))

# 2. 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('No', end=' ')