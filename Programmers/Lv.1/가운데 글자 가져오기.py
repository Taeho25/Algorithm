'''Lv.1 가운데 글자 가져오기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12903


# 풀이 1
def solution(s):
    idx = len(s) // 2
    
    if(len(s) % 2 == 1):
        return s[idx]
    else:
        return s[idx-1]+s[idx]