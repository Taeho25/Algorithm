'''Lv.2 튜플'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/64065


# 풀이 1 : 먼저 나오는 숫자부터 넣기
def solution(s):
    # 1. 전처리 : 문자열에서 그룹 추출
    s = s[2:-2].split('},{')
    s.sort(key=lambda x: len(x))
    #print(s)

    # 2. 전처리2 : 각 그룹별 리스트화
    items = []
    for item in s:  # 
        item = list(map(int, item.split(',')))
        items.append(item)
    #print(items)
    
    # 3. 추가된 숫자 하나씩 넣기 (차집합 이용)
    answer = [items[0][0]]
    for items_idx in range(0, len(items)-1):
        number = set(items[items_idx+1]) - set(items[items_idx])
        answer.append(number.pop()) # 집합 원소 접근법
    
    return answer


# 풀이 2
def solution(s):
    # 1. 전처리 : 문자열에서 그룹 추출
    s = s[2:-2].split('},{')
    s.sort(key=lambda x: len(x))
    #print(s)

    # 2. 전처리2 : 각 그룹별 리스트화
    items = []
    for item in s:  # 
        item = list(map(int, item.split(',')))
        items.append(item)
    #print(items)
    
    # 3. items 내 각 item에서 추가된 number 확인 후 answer에 넣기
    answer = []
    for item in items:
        for number in item:
            if number not in answer:
                answer.append(number)
    
    return answer


# 풀이 3 
def solution(s):
    # 1. 전처리 : 문자열에서 그룹 추출
    s = s[2:-2].split("},{")
    s.sort(key=lambda x: len(x))
    
    # 2. items 내 각 item에서 추가된 number 확인 후 answer에 넣기
    answer = []
    for item in s:
        item = list(map(int, item.split(",")))
        for number in item:
            if number not in answer:
                answer.append(number)

    return answer


# 풀이 4 : 많이 나오는 숫자부터 넣기
import re
from collections import Counter

def solution(s):
    # 1. 전처리 : 숫자(정규식으로 확인)들의 개수 정보 정리
    s = Counter(re.findall('\d+', s))
    #print(s)
    
    # 2. 정렬 : 개수 많은 순
    items = sorted(s.items(), key=lambda x: x[1], reverse=True)
    #print(items)
    
    # 3. 순서대로 넣기
    answer = [int(number) for number, value in items]
    #print(answer)
    
    return answer


# 풀이 5 (풀이 4 축약)
import re
from collections import Counter
def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))