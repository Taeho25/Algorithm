'''Lv.1 직사각형 별찍기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12969


# 풀이
n, m = map(int, input().split())
for row in range(m):
    print('*'*n)