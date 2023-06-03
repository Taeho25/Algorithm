'''Lv.1 푸드 파이트 대회'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/134240


# 풀이 1
def solution(food):
    table1 = [str(i) * (n//2) for i, n in enumerate(food)]
    table2 = sorted(table1, reverse=True)
    return "".join(table1) + "0" + "".join(table2)


# 풀이 2
def solution(food):
    table1 = "".join([str(i) * (n//2) for i, n in enumerate(food)])
    table2 = table1[::-1]
    return table1 + "0" + table2