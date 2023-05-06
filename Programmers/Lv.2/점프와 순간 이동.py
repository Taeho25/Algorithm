'''Lv.2 점프와 순간 이동'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12980


# 풀이 1
def solution(n):
    answer = 0
    
    while(n > 0):
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
    
    return answer


# 풀이 2
def solution(n):
    answer = 0
    
    while (n > 0):
        answer += n % 2  # n이 홀수면 알아서 answer += 1 해줌
        n = n // 2       # n이 홀수면 알아서 n -= 1 해줌

    return answer


# 풀이 3
def solution(n):

    return bin(n).count('1')