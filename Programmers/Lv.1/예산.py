'''Lv.1 예산'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12982


# 풀이 1
def solution(d, budget):
    answer = 0
    d.sort()
    for d_money in d:
        if budget >= d_money:
            budget -= d_money
            answer += 1
        else: break
    return answer

  
# 풀이 2
def solution(d, budget):
    answer = 0
    d.sort()
    for d_money in d :
        budget -= d_money
        if budget < 0: break
        answer += 1
    return answer
