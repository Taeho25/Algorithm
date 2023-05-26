'''Lv.0 특정 문자 제거하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120826


# 풀이 1
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer