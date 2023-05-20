'''Lv.2 귤 고르기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/138476


# 풀이 1
from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)
    sorted_c = sorted(cnt.items(), key=lambda x: -x[1])
    
    for size, num in sorted_c:
        k -= num
        answer += 1
        if k <= 0: break
    
    return answer


# 풀이 2
from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)

    for num in sorted(cnt.values(), reverse = True):
        k -= num
        answer += 1
        if k <= 0: break

    return answer


# 풀이 3
from collections import Counter

def solution(k, tangerine):
    cnt = Counter(tangerine)
    tangerine.sort(key = lambda t: (-cnt[t], t))
    answer = len(set(tangerine[:k]))
    
    return answer