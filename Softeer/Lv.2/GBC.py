'''Lv.2 - GBC'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=584


# 풀이 1
import sys
input = sys.stdin.readline

# 1, 데이터 입력
N, M = map(int, input().split())
limit = []
for _ in range(N):
    length, speed = map(int, input().split())
    for _ in range(length):
        limit.append(speed)

# 2. 테스트 데이터와 제한 속도 비교
i = 0
result = 0
for _ in range(M):
    test_length, test_speed = map(int, input().split())
    for _ in range(test_length):
        if limit[i] < test_speed:
            result = max(result, test_speed - limit[i])
        i += 1

# 3. 결과 출력
print(result)