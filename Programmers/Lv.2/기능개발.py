'''Lv.1 기능개발'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42586


# 풀이 1
import math
def solution(progresses, speeds):
    days = []
    
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)
        days.append(day)

    answer = []
    release = 0
    j = 1
    cnt = 1
    while(1):
        if days[release] >= days[j]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            release = j
        j += 1
        
        if j == len(days):
            answer.append(cnt)
            break
    
    return answer


# 풀이 2
def solution(progresses, speeds):
    days = []

    for progress, speed in zip(progresses, speeds):
        day = -((progress - 100) // speed)
        if (len(days) == 0) or ((days[-1][0] < day)):
            days.append([day, 1])
        else:
            days[-1][1] += 1
    
    answer = []
    for day in days:
        answer.append(day[1])
    
    return answer


# 풀이 3
def solution(progresses, speeds):
    days = []

    for progress, speed in zip(progresses, speeds):
        if (len(days) == 0) or ((days[-1][0] < -((progress - 100) // speed))):
            days.append([-((progress - 100) // speed), 1])
        else:
            days[-1][1] += 1
            
    return [day[1] for day in days]