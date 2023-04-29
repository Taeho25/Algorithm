'''Lv.1 부족한 금액 계산하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/82612


# 풀이 1
def solution(price, money, count):
    answer = price * count * (count + 1) / 2 - money
    if answer <= 0: answer = 0

    return answer


# 풀이 2
def solution2(price, money, count):
    total_price = 0
    for i in range(1, count+1):
        total_price += i * price
    
    if total_price - money >= 0: return total_price - money
    else: return 0