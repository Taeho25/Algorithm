'''Lv.2 구명보트'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42885


# 풀이 1
def solution(people, limit):
    answer = 0
    people.sort()
    small_p, big_p = 0, len(people) - 1
    
    while small_p <= big_p:
        answer += 1
        if people[small_p] + people[big_p] <= limit:
            small_p += 1
            big_p -= 1
        elif small_p == big_p:
            break
        else:
            big_p -= 1
    
    return answer

  
# 풀이 2
def solution(people, limit) :
    answer = 0
    people.sort()
    small_p, big_p = 0, len(people) - 1

    while small_p < big_p:
        if people[small_p] + people[big_p] <= limit:
            small_p += 1
            answer += 1
        big_p -= 1
        
    return len(people) - answer  # 전체 인원수 - 두 명 탑승 보트 수

  
# 풀이 3
from collections import deque
def solution(people, limit):
    answer = 0
    deque_people = deque(sorted(people))

    while deque_people:
        small_p = deque_people.popleft()
        if not deque_people:
            return answer + 1
        big_p = deque_people.pop()
        if small_p + big_p > limit:
            deque_people.appendleft(small_p)
        answer += 1

    return answer