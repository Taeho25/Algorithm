'''Lv.2 [1차] 뉴스 클러스터링'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/17677


# 풀이 1
def solution(str1, str2):
    # 1. s1 전처리
    s1 = []
    for i in range(len(str1)-1):
        element = str1[i:i+2]
        if element.isalpha(): 
            s1.append(element.lower())
    #print(s1)
    
    # 2. s2 전처리 
    s2 = []
    for i in range(len(str2)-1):
        element = str2[i:i+2]
        if element.isalpha(): 
            s2.append(element.lower())
    #print(s2)
    
    # 3. 교집합원소개수, 합집합원소개수 계산
    cnt_gyo = 0
    for element in s1:
        if element in s2:
            cnt_gyo += 1
            s2[s2.index(element)] = ''
    cnt_hap = len(s1) + len(s2) - cnt_gyo
    
    # 4. J 구하기
    if cnt_hap == 0:
        return 65536
    else:
        return int(cnt_gyo / cnt_hap * 65536)
    

# 풀이 2
def solution(str1, str2):
    # 1. s1 전처리
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    # 2. 교집합원소개수, 합집합원소개수 계산
    gyo = set(str1) & set(str2)
    cnt_gyo = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    cnt_hap = len(s1) + len(s2) - cnt_gyo
    
    # 4. J 구하기
    if cnt_hap == 0:
        return 65536
    else:
        return int(cnt_gyo / cnt_hap * 65536)


# 풀이 3
import re
import math
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    cnt_gyo = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    cnt_hap = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((cnt_gyo/cnt_hap)*65536)


# 풀이 4
from collections import Counter
def solution(str1, str2):
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)

    gyo = c1&c2
    hap = c1|c2
    cnt_gyo = sum(gyo.values())
    cnt_hap = sum(hap.values())

    answer = int(cnt_gyo / cnt_hap * 65536)

    return answer