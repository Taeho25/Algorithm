'''Lv.2 금고 털이'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=395


# 풀이 1
import sys
input = sys.stdin.readline

# 1. 배낭 무게 W, 귀금속 종류 N 입력
w, n = map(int, input().split())

# 2. N개의 금속무게 m과 무게당 가격 p 입력
mps = []
for i in range(n):
    mp = tuple(map(int, input().split()))
    mps.append(mp)

# 3. 비싼 귀금속 순으로 정렬(귀금속 가격 오름차순)
mps.sort(reverse=True, key=lambda x: x[1])

# 4. 비싼 귀금속부터 배낭에 담기
result = 0
for i in range(n):
    if w > mps[i][0]:
        result += mps[i][0] * mps[i][1]
        w -= mps[i][0]
    else:
        result += w * mps[i][1]
        break

print(result)