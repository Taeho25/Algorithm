'''Lv.0 배열 조각하기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181893


# 풀이 1
def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        elif i % 2 == 1:
            arr = arr[query[i]:]

    return arr
