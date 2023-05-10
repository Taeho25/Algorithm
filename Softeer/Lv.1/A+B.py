'''Lv.1 A+B'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=362


# 풀이 1
import sys

T = int(input())
ans = []

for i in range(T):
    A, B = sys.stdin.readline().split()
    ans.append(int(A) + int(B))

for i in range(T):
    print(f'Case #{i+1}: {ans[i]}')