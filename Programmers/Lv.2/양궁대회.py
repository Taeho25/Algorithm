'''Lv.2 양궁대회'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/92342


# 풀이 1
from itertools import product

def solution(n, info):
    info.reverse()
    answer = [-1]
    max_gap = 0
    
    for win in product((True, False), repeat=11):
        # 라이언이 가져가는 점수의 화살 수
        num_arrow = sum(info[i]+1 for i in range(11) if win[i])

        # 라이언이 가져가는 점수의 화살 수 <= 총 화살 수 : 말이 됨
        if num_arrow <= n:
            # 점수
            apeach_score = sum(i for i in range(11) if not win[i] and info[i]) # 라이언이 지거나 비김
            ryan_score = sum(i for i in range(11) if win[i]) # 라이언이 이김
            gap = ryan_score - apeach_score
            if gap > max_gap:
                max_gap = gap
                answer = [info[i]+1 if win[i] else 0 for i in range(11)]
                answer[0] += n - num_arrow  # 남은 화살은 0점에
    answer.reverse()

    return answer
    

# 풀이 2
from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear()
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]
