# [25] 이진 탐색 - 부품 찾기 by 집합 자료형


# 1. 부품개수 N / 부품목록 array / 확인부품개수 m / 확인부품목록 x 입력
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('No', end=' ')