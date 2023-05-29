'''Lv.3 스마트 물류'''

# 문제 : https://www.softeer.ai/practice/info.do?idx=1&eid=414


# 풀이 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
PHs = list(input().rstrip())

answer = 0
for idx in range(n):
    if PHs[idx] == 'P':
        for i in range(-k, k+1):
            if idx+i < 0 or idx+i >= n:
                continue
            if PHs[idx + i] == 'H':
                answer += 1
                PHs[idx + i] = ' '
                break

print(answer)