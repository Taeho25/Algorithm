'''Lv.1 성격 유형 검사하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/118666


# 풀이 1
def solution(survey, choices):
    answer = ''
    result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    type1 = ['R', 'C', 'J', 'A']
    type2 = ['T', 'F', 'M', 'N']
    
    for sur, choice in zip(survey, choices):
        if choice < 4:
            result[sur[0]] += (4 - choice)
        else:
            result[sur[1]] += (choice - 4)
    
    answer = ""
    for t1, t2 in zip(type1, type2):
        if result[t1] >= result[t2]:
            answer += t1
        else:
            answer += t2

    return answer


# 풀이 2
def solution(survey, choices):
    answer = ''
    result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    type1 = ['R', 'C', 'J', 'A']
    type2 = ['T', 'F', 'M', 'N']
    
    for sur, choice in zip(survey, choices):
        result[sur[0]] += (4 - choice)
    
    answer = ""
    for t1, t2 in zip(type1, type2):
        if result[t1] >= result[t2]:
            answer += t1
        else:
            answer += t2

    return answer


# 풀이 3
def solution3(survey, choices):
    answer = ''
    rtcfjman = [0, 0, 0, 0, 0, 0, 0, 0]
    str = "RTCFJMAN"
    
    for i in range(len(survey)):
        rtcfjman[str.index(survey[i][0])] += 4 - choices[i]

    if(rtcfjman[0] >= rtcfjman[1]): answer += "R"
    else: answer += "T"
    if(rtcfjman[2] >= rtcfjman[3]): answer += "C"
    else: answer += "F"
    if(rtcfjman[4] >= rtcfjman[5]): answer += "J"
    else: answer += "M"
    if(rtcfjman[6] >= rtcfjman[7]): answer += "A"
    else: answer += "N"

    return answer
