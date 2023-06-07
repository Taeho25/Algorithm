'''Lv.2 행렬의 곱셈'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12949


# 풀이 1
def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    answer = [[0]*col for _ in range(row)]
    
    for r in range(row):
        for c in range(col):
            for idx in range(len(arr1[0])):
                answer[r][c] += arr1[r][idx] * arr2[idx][c]

    return answer


# 풀이 2 : unpacking 개념 - zip(*arr2)
def solution(arr1, arr2):

    return [[sum(a1_r*a2_c for a1_r, a2_c in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]


# 풀이 3
import numpy as np

def solution(arr1, arr2):

    return (np.matrix(arr1)*np.matrix(arr2)).tolist()