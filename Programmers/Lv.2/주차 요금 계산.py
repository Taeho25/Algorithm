'''Lv.2 주차 요금 계산'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/92341


# 풀이 1
import math

def solution(fees, records):
    answer = []
    data = {}
    
    # 1. ID별 출입 시간 데이터 전처리
    for record in records:
        time, ID, op = record.split()
        if ID not in data:
            data[ID] = []
        data[ID].append(time)
        
    # 2. 데이터를 리스트로 변경, 출입데이터 개수 홀수개면 '23:59' 추가, ID 기준 정렬
    data_list = []
    for ID in data:
        if len(data[ID]) % 2 == 1:
            data[ID].append('23:59')
        data_list.append((int(ID), data[ID]))
    data_list.sort(key=lambda x: x[0])
    
    # 3. 주차 요금 게산
    for data in data_list:
        time_stemp = [-(int(t[:2])*60 + int(t[3:])) if i%2==0 else int(t[:2])*60 + int(t[3:]) for i, t in enumerate(data[1])]
        time = sum(time_stemp)
        
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + math.ceil((time - fees[0])/fees[2]) * fees[3]
            answer.append(fee)
        
    return answer
