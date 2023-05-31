'''Lv.2 연속 부분 수열 합의 개수'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/131701


# 풀이 1
def solution(elements):
    answer = set()
    elements2 = elements*2
    for i in range(1, len(elements)):
        for s in range(len(elements)):
            #print(elements2[s:s+i])
            temp = sum(elements2[s:s+i])
            answer.add(temp)
        
    return len(answer)+1