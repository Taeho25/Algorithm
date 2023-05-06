'''Lv.1 이진 변환 반복하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/70129


# 풀이 1
def solution(s):
    answer = [0, 0]
    
    while(s != '1'):
        answer[0] += 1
        s2 = s.replace('0', '')
        answer[1] += len(s) - len(s2)
        s = bin(len(s2))[2:]    
    
    return answer