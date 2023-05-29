'''Lv.3 성적 평균'''

# 문제 : https://www.softeer.ai/practice/info.do?idx=1&eid=389


# 풀이 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))

for _ in range(k):
    start, end = map(int, input().split())
    sum_scores = sum(scores[start-1:end])
    num_scores = end - start + 1
    avg_scores = round(sum_scores / num_scores, 2)
    print(avg_scores)