'''Lv.2 할인 행사'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/131127


# 풀이 1
def solution(want, number, discount):
    for w in want:
        if w not in discount:
            return 0
        
    answer = 0
    
    check_list = [0]*len(want)
    for i, item in enumerate(discount):
        if i < 10:
            if item in want:
                idx = want.index(item)
                check_list[idx] += 1
        else:
            if discount[i-10] in want:
                del_idx = want.index(discount[i-10])
                check_list[del_idx] -= 1
            if item in want:
                idx = want.index(item)
                check_list[idx] += 1
        
        if check_list == number:
            answer += 1
    
    return answer


# 풀이 2
from collections import Counter

def solution(want, number, discount):
    check_dic = {}
    for i, w in enumerate(want):
        check_dic[w] = number[i]

    answer = 0
    for i in range(len(discount)-9):
        if check_dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer