'''Lv.1 최대공약수와 최소공배수'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12940


# 풀이 1
import math
def solution(n, m):
    answer = []
    
    def lcm(n, m):
        return (n * m) // math.gcd(n, m)
    
    nm_gcd = math.gcd(n, m)
    nm_lcm = lcm(n, m)
    answer = [nm_gcd, nm_lcm]

    return answer


# 풀이 2
def solution2(n, m):    # 유클리드 호제법 이용
    num1, num2 = max(n, m), min(n, m)

    remainder = 1
    while remainder > 0:    # remainder = 0 : num1이 num2로 나누어 떨어질 때 까지
        remainder = num1 % num2
        num1, num2 = num2, remainder
    
    answer = [num1, int(n * m / num1)]
    return answer
