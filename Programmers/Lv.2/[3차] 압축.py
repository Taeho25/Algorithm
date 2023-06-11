'''Lv.2 [3차] 압축'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/17684


# 풀이 1
def solution(msg):
    dictionary = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X', 'Y', 'Z']
    answer = []
    flag = True
    s = 0  # s: 첫 글자 인덱스
    
    while(flag):
        f = s  # f: 끝 글자 인덱스

        while(True):
            if msg[s:f+1] not in dictionary:
                answer.append(dictionary.index(msg[s:f]))
                dictionary.append(msg[s:f+1])
                break
            elif f == len(msg)-1:
                answer.append(dictionary.index(msg[s:f+1]))
                flag = False
                break
            else:
                f += 1
        s = f         
            
    return answer


# 풀이 2
def solution(msg):
    dictionary = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    answer = []

    while True:
        if msg in dictionary:  # 마무리
            answer.append(dictionary.index(msg))
            break

        for f in range(len(msg)):  # 끝 글자 인덱스
            if msg[:f+1] not in dictionary:
                answer.append(dictionary.index(msg[:f]))
                dictionary.append(msg[:f+1])
                msg = msg[f:]
                break

    return answer


# 풀이 3
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = {k:v for (k, v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in dictionary:  # 마무리
            answer.append(dictionary[msg])
            break
        
        for f in range(1, len(msg) + 1):  # 끝 글자 + 1 인덱스
            if msg[:f] not in dictionary:
                answer.append(dictionary[msg[0:f-1]])
                dictionary[msg[:f]] = len(dictionary)+1
                msg = msg[f-1:]
                break

    return answer