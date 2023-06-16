'''Lv.2 주식가격'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42584


# 풀이 1 : 정확성 테스트 10/10, 효율성 테스트 0/5
def solution(prices):
    answer = [0]*len(prices)
    end_flag = [False]*len(prices)
    
    for now in range(1, len(prices)):
        for pre in range(0, now):
            if end_flag[pre] != True:
                if prices[pre] > prices[now]:
                    end_flag[pre] = True
                answer[pre] += 1
                    
    return answer


# 풀이 2 : 정확성 테스트 10/10, 효율성 테스트 3/5
def solution(prices):
    answer = []
    
    for i, this_price in enumerate(prices):
        for sec in range(1, len(prices)-i):
            if this_price > prices[i + sec]:
                answer.append(sec)
                break
            elif sec == len(prices)-i-1:
                answer.append(sec)     
    answer.append(0)
    
    return answer