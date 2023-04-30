'''Lv.1 이상한 문자 만들기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12930


# 풀이 1
def solution(s):
    answer =""
    word_cnt = -1
    
    for word in s:
        word_cnt += 1
        if word == ' ':
            answer += ' '
            word_cnt = -1
        elif word_cnt % 2 == 0:
            answer += word.upper()
        else:
            answer += word.lower()
    
    return answer


# 풀이 2
