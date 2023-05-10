'''Lv.1 근무 시간'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=990


# 풀이 1
import sys

result = 0
for _ in range(5):
    St, Ft = sys.stdin.readline().split()
    St = int(St[:2])*60 + int(St[3:])
    Ft = int(Ft[:2])*60 + int(Ft[3:])
    result += (Ft - St)

print(result)