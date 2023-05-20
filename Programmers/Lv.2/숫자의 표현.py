'''Lv.2 숫자의 표현'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12924


# 풀이 1
def solution(n):
    # i개 더할 때 숫자들 : m+0, m+1, ... , m+(i-1)
    answer = 0

    for i in range(1, n+1):
        sum_i = (i-1) * i / 2  # 1 ~ n 더하기 공식 = n*(n+1) / 2
        sum_m = n - sum_i
        if sum_m <= 0: break
        if sum_m % i == 0:
            answer += 1

    return answer


# 풀이 2
def solution(n):
    answer = 0

    for mi in range(1, n+1):
        sum_mi = 0

        while (sum_mi < n):
            sum_mi += mi
            mi += 1
        if sum_mi == n:
            answer += 1

    return answer


# 풀이 3
def solution(n):
    answer = 0

    for mi in range(1, n+1):
        sum_mi = 0

        for mis in range(mi, n+1):
            sum_mi += mis
            if sum_mi > n: break
            if sum_mi == n:
                answer += 1
                break

    return answer