'''Lv.2 지도 자동 구축'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=413


# 풀이 1
N = int(input())

ans = 2
for i in range(N):
    ans = ans * 2 - 1

print(ans**2)