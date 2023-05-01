'''Lv.1 [1차] 비밀지도'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/17681


# 풀이 1
def solution(n, arr1, arr2):
    bin_arr1 = []
    for a1 in arr1:
        b1 = bin(a1)[2:]
        bin_arr1.append(b1.zfill(n))
    
    bin_arr2 = []
    for a2 in arr2:
        b2 = bin(a2)[2:]
        bin_arr2.append(b2.zfill(n))
    
    answer = []
    for row in range(n):
        tmp = ''
        for col in range(n):
            if bin_arr1[row][col] == '1' or bin_arr2[row][col] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
        
    return answer


# 풀이 2
def solution2(n, arr1, arr2):
    temp = []
    for a1, a2 in zip(arr1, arr2):
        a12 = bin(a1 | a2)[2:]
        a12 = a12.zfill(n)
        temp.append(a12)
    
    answer = []
    for num in temp:
        num = num.replace('1', '#')
        num = num.replace('0', ' ')
        answer.append(num)
        
    return answer


# 풀이 3
def solution3(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a12 = bin(a1 | a2)[2:]
        a12 = a12.rjust(n, '0')    # rjust(n, '0') == zfill(n)
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
        
    return answer