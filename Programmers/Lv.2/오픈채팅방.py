'''Lv.2 오픈채팅방'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42888


# 풀이 1 : answer_data 데이터 전처리 -> answer 데이터 생성
def solution(record):
    answer = []
    ID = {}
    
    # 1. ID-닉네임 매칭
    for rec in record:
        data = rec.split()
        if data[0] != "Leave":
            ID[data[1]] = data[2]
        
    # 2. answer 데이터 생성
    for rec in record:
        data = rec.split()
        if data[0] == "Enter":
            answer.append(ID[data[1]] + "님이 들어왔습니다.")
        elif data[0] == "Leave":
            answer.append(ID[data[1]] + "님이 나갔습니다.")
    
    return answer