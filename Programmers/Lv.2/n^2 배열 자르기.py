'''Lv.2 n^2 배열 자르기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/87390


# 풀이 1 (시간초과)
def solution(n, left, right):
    array = [[0]*n for i in range(n)]
               
    i = 1
    while (i <= n):
        for row in range(i):
            for col in range(i):
                if array[row][col] == 0:
                    array[row][col] = i
        i += 1
        
    answer = []
    for i in range(n):
        answer += array[i]
        
    return answer[left:right+1]


# 풀이 2
def solution(n, left, right):
    array = []
            
    for idx in range(left, right+1):
        row = idx // n
        col = idx % n
        array.append(max(row, col)+1)
        
    return array