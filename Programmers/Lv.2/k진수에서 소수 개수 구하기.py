'''Lv.2 k진수에서 소수 개수 구하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/92335


# 풀이 1
def isPrime(P):
    for n in range(2, int(P**0.5)+1):
        if P % n == 0:
            return False
    return True

def solution(n, k):
    n_k = ""
    while(n>0):
        n_k = str(n%k) + n_k
        n //= k
    
    Ps = [int(P) for P in n_k.split('0') if P not in ['', '1']]
    
    answer = 0
    for P in Ps:
        if isPrime(P):
            answer += 1
            
    return answer


# 풀이 2
def isPrime(P):
    for n in range(2, int(P**0.5)+1):
        if P % n == 0:
            return False
    return True

def solution(n, k):
    n_k = ""
    while(n>0):
        n_k = str(n%k) + n_k
        n //= k

    answer = 0
    for P in n_k.split('0'):
        if P not in ['', '1'] and isPrime(int(P)):
            answer += 1
            
    return answer