'''Lv.1 주행거리 비교하기'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=1016


# 풀이 1
import sys

A, B = map(int, sys.stdin.readline.split())

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('same')