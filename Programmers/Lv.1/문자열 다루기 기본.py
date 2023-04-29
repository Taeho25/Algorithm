'''Lv.1 문자열 다루기 기본'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12918


# 풀이 1
def solution(s):
    if len(s) != 4 and len(s) != 6: return False
    
    for word in s:
        if word >= '0' and word <= '9': continue
        else: return False
    return True


# 풀이 2
def solution2(s):
    return s.isdecimal() and len(s) in [4,6]


# 풀이 3
def solution3(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6


# 풀이 4
def solution4(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
        except:
            return False
    else: return False
    return True