'''Lv.2 타겟 넘버'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43165


# 풀이 1
def solution(numbers, target):
    answer = 0
    
    for ops in range(2**len(numbers)):
        ops_bin = '0'*(len(numbers)-len(bin(ops)[2:])) + bin(ops)[2:]
        ops_list = list(ops_bin)
        
        ssum = 0
        for op, number in zip(ops_list, numbers):
            if op == '0':
                ssum += number
            else:
                ssum -= number
        
        if ssum == target:
            answer += 1
        
    return answer


# 풀이 2
from itertools import product

def solution(numbers, target):
    answer = 0
    nums_set = [(x, -x) for x in numbers]
    
    for nums in product(*nums_set):
        ssum = sum(nums)
        
        if ssum == target:
            answer += 1
    
    return answer


# 풀이 3
from itertools import product

def solution(numbers, target):
    nums_set = [(x, -x) for x in numbers]

    ssum_list = list(map(sum, product(*nums_set)))

    return ssum_list.count(target)


# 풀이 4 : DFS
def dfs(nums, i, n, t):
    ret = 0

    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    
    return answer