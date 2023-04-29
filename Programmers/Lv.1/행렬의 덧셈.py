'''Lv.1 행렬의 덧셈'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12950


# 풀이 1
def solution(arr1, arr2):
    for row in range(len(arr1)):
        for col in range(len(arr1[0])):
            arr1[row][col] += arr2[row][col]
    return arr1


# 풀이 2
import numpy as np
def solution2(arr1, arr2):
    A1_np = np.array(arr1)
    A2_np = np.array(arr2)
    result = A1_np + A2_np
    return result.tolist()


# 풀이 3
def solution3(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    answer = [[arr1[i][j] + arr2[i][j] for j in range(m)] for i in range(n)]
    return answer