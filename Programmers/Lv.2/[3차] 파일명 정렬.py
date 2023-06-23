'''Lv.2 [3차] 파일명 정렬'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/17686


# 풀이 1
def solution(files):
    data = []
    
    # 1. 전처리
    for file in files:
        data.append(["", ""])
        file = file.lower()
        
        mode = 0
        for c in file:
            if not c.isdecimal():  # head 처리
                if mode == 1: break
                data[-1][0] += c
            else:  # number 처리
                data[-1][1] += c
                mode = 1

        data[-1][1] = int(data[-1][1])
    
    # 2. 정렬
    answer = sorted(files, key=lambda f: (data[files.index(f)][0], data[files.index(f)][1]))
    
    return answer


# 풀이 2
def solution(files):
    data = []
    
    # 1. 전처리
    for idx, file in enumerate(files):
        data.append([idx, "", ""])
        file = file.lower()
        
        mode = 0
        for c in file:
            if not c.isdecimal():  # head 처리
                if mode == 1: break
                data[-1][1] += c
            else:  # number 처리
                data[-1][2] += c
                mode = 1

        data[idx][2] = int(data[idx][2])
    
    # 2. 정렬
    data.sort(key=lambda x: (x[1], x[2]))
    answer = [files[i] for i,h,n in data]
    
    return answer


# 풀이 3 : 정규표현식
import re

def solution(files):
    data = [re.split('([0-9]+)', file) for file in files]
    data = sorted(data, key = lambda x : (x[0].lower(), int(x[1])))

    return ["".join(d) for d in data]