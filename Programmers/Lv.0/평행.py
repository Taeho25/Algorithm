'''Lv.0 평행'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120875


# 풀이 1
def solution(dots):
    # 0-1, 2-3
    line01 = (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0])
    line23 = (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0])
    # 0-2, 1-3
    line02 = (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0])
    line13 = (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0])
    # 0-3, 1-2
    line03 = (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0])
    line12 = (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0])
    
    if line01 == line23 or line02 == line13 or line03 == line12:
        return 1
    else:
        return 0
    

# 풀이 2
