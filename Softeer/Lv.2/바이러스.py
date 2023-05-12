'''Lv.2 바이러스'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=407


# 풀이 1
import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

for i in range(n):
    k = (k * p) % 1000000007
    
print(k)