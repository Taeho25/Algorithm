'''Lv.2 프로세스'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42587


# 풀이 1
from collections import deque
def solution(priorities, location):
    # 1. 전처리
    data = []
    for idx in range(len(priorities)):
        data.append((idx, priorities[idx]))
    queue = deque(data)
    
    # 2. 작업
    answer = 0
    while(queue):
        # 2-1. 문제 1번 절차
        cur_process = queue.popleft()

        # 2-2. 문제 2번 절차
        before_run = len(queue)
        for q in queue:
            if cur_process[1] < q[1]:
                queue.append(cur_process)
                break
        after_run = len(queue)
        
        # 2-3. 문제 3번 절차
        if before_run == after_run:
            answer += 1
            if cur_process[0] == location:
                break

    return answer


# 풀이 2
from collections import deque
def solution(priorities, location):
    # 1. 전처리
    data = []
    for idx, priority in enumerate(priorities):
        data.append((idx, priority))
    queue = deque(data)
    
    # 2. 작업
    answer = 0
    while(queue):
        # 2-1. 문제 1번 절차
        cur_process = queue.popleft()

        # 2-2. 문제 2번 절차
        before_run = len(queue)
        for q in queue:
            if cur_process[1] < q[1]:
                queue.append(cur_process)
                break
        after_run = len(queue)
        
        # 2-3. 문제 3번 절차
        if before_run == after_run:
            answer += 1
            if cur_process[0] == location:
                break

    return answer

# 풀이 3
from collections import deque
def solution(priorities, location):
    # 1.
    data =  [(idx, priority) for idx, priority in enumerate(priorities)]
    queue = deque(data)

    # 2.
    answer = 0
    while True:
        # 2-1.
        cur_process = queue.popleft()

        # 2-2.
        if any(cur_process[1] < q[1] for q in queue):
            queue.append(cur_process)
        # 2-3.
        else:
            answer += 1
            if cur_process[0] == location:
                return answer
            

# 풀이 4
def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor % jobs]:
            priorities[cursor % jobs] = 0
            answer += 1
            if cursor % jobs == location:
                break
        cursor += 1

    return answer