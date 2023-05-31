'''Lv.2 연속 부분 수열 합의 개수'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/131701


# 풀이 1
def solution(elements):
    ele_len = len(elements)
    answer = set()
    elements = elements * 2

    for i in range(1, ele_len + 1):
        for s in range(ele_len):
            #print(elements2[s:s+i])
            ssum = sum(elements[s:s+i])  # 이중for문 + sum() -> O(N^3)
            answer.add(ssum)
        
    return len(answer)


# 풀이 2
def solution(elements):
    ele_len = len(elements)
    answer = set(elements)  # 부분수열 길이가 1인 경우의 합으로 초기화
    elements = elements * 2

    for s in range(2, ele_len):
        for i in range(ele_len):
            ssum = sum(elements[s:s+i])  # 이중for문 + sum() -> O(N^3)
            answer.add(ssum)

    return len(answer) + 1


# 풀이 3
def solution(elements):
    ele_len = len(elements)
    answer = set()

    for s in range(ele_len):
        ssum = elements[s]
        answer.add(ssum)
        for i in range(s+1, s+ele_len):
            ssum += elements[i % ele_len]  # 이중for문 + ssum 사용 -> O(N^2)
            answer.add(ssum)
            
    return len(answer)


# 풀이 4
def solution(elements):
    ele_len = len(elements)
    answer = set()

    for s in range(ele_len):
        ssum = elements[s]
        answer.add(ssum)
        for i in range(s+1, s+ele_len-1):
            ssum += elements[i % ele_len]
            answer.add(ssum)
            
    return len(answer) + 1
