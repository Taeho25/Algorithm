'''Lv.2 H-Index'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42747


# 풀이 1
def solution(citations):
    answer = 0
    citations.sort()
    
    for idx in range(len(citations)):
        if  citations[idx] >= len(citations) - idx:
            answer += 1
            
    return answer
  

# 풀이 2
def solution(citations):
    citations.sort(reverse=True)
    
    for idx in range(len(citations)):
        if citations[idx] <= idx:
            return idx
    
    return len(citations)