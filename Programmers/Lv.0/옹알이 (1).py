'''Lv.2 옹알이 (1)'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120956


# 풀이 1
def solution(babbling):
    answer = 0
    joca_words = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for joca_word in joca_words:
            word = word.replace(joca_word, " ")
        
        if word.strip() == "":
            answer += 1

    return answer


# 풀이 2
import re
def solution(babbling):
    answer = 0
    joca_words = re.compile('^(aya|ye|woo|ma)+$')
    
    for word in babbling:
        if joca_words.match(word):
            answer += 1

    return answer
