'''Lv.1 크기가 작은 부분 문자열'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/147355


# 풀이 1
def solution(t, p):
    check_len = len(t) - len(p) + 1
    cnt = 0
    for i in range(check_len):
        part_num = t[i:i+len(p)]
        if int(part_num) <= int(p): cnt += 1
    return cnt