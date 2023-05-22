'''Lv.3 징검다리'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=390


# 풀이 1
import sys
input = sys.stdin.readline

# 1. N, Ai 입력
n = int(input().rstrip())
stones = list(map(int, input().split()))

# 2. 돌 두 개씩 비교
steps = [1]*n
for r_idx in range(1, n):
    max_height = 0
    for l_idx in range(r_idx):
        if stones[l_idx] < stones[r_idx]:
            if max_height < steps[l_idx]:
                max_height = steps[l_idx]
    steps[r_idx] = max_height + 1

# 3. 결과 출력
print(max(steps))