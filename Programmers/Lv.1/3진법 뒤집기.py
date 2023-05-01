'''Lv.1 3진법 뒤집기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/68935


# 풀이 1
def solution(n):
    temp = []
    while(n>0):
        temp.append(n % 3)
        n //= 3

    answer = 0
    for idx in range(len(temp)):
        answer += pow(3,idx) * temp[(-1)*(idx+1)]
        
    return answer


# 풀이 2
def solution2(n):
    temp = ''
    while n:
        temp += str(n % 3)
        n = n // 3

    answer = int(temp, 3)   # int()의 비밀 : 3진수 temp를 10진수로 변환
    return answer