'''Lv.1 K번째수'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42748


# 풀이 1
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        new_array = array[i-1:j]
        new_array.sort()
        ans = new_array[k-1]
        answer.append(ans)
        
    return answer