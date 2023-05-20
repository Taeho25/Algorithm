'''Lv.2 최솟값 만들기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12941


# 풀이 1
def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]
        
    return answer


# 풀이 2
def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        answer += a*b
        
    return answer


# 풀이 3
def solution(A,B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])