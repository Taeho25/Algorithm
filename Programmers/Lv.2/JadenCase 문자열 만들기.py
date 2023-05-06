'''Lv.1 JadenCase 문자열 만들기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12951


# 풀이 1 (틀린 풀이)
def solution(s):
    words = s.split()
    for word in words:
        word_new = word[0].upper() + word[1:].lower()
        s = s.replace(word, word_new)
        
    return s


# 풀이 2
def solution(s):
    check_pre_blank = True
    answer = ""
    for word in s:
        if word == ' ':
            answer += word
            check_pre_blank = True
        else:
            if check_pre_blank:
                answer += word.upper()
            else:
                answer += word.lower()
            check_pre_blank = False
            
    return answer