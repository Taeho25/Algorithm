'''Lv.1 최댓값과 최솟값'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12939


# 풀이 1
def solution(s):
    nums = list(map(int, s.split()))

    return str(min(nums)) + " " + str(max(nums))


# 풀이 2
def solution(s):
    nums = s.split()
    n = [int(i) for i in nums]
    n.sort()

    return str(n[0]) + " " + str(n[-1])