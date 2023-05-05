'''Lv.1 로또의 최고 순위와 최저 순위'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/77484


# 풀이 1
def solution(lottos, win_nums):
    cnt_yes = 0
    cnt_0 = lottos.count(0)
    
    for lotto in lottos:
        if lotto in win_nums:
            cnt_yes += 1
    
    rank_max = 7 - (cnt_yes + cnt_0)
    if rank_max == 7: rank_max = 6
    rank_min = 7 - cnt_yes
    if rank_min == 7: rank_min = 6
    
    return [rank_max, rank_min]


# 풀이 2
def solution2(lottos, win_nums):
    cnt_yes = len([x for x in lottos if x in win_nums])
    cnt_0 = lottos.count(0)

    rank_max = 7 - (cnt_yes + cnt_0) if (cnt_yes + cnt_0) >= 1 else 6
    rank_min = 7 - cnt_yes if cnt_yes >= 1 else 6

    return [rank_max, rank_min]


# 풀이 3
def solution3(lottos, win_nums):
    rank=[6, 6, 5, 4, 3, 2, 1]
    cnt_yes = 0
    cnt_0 = lottos.count(0)

    for lotto in lottos:
        if lotto in win_nums:
            cnt_yes += 1

    return [rank[cnt_yes + cnt_0], rank[cnt_yes]]


# 풀이 4
def solution4(lottos, win_nums):
    rank=[6, 6, 5, 4, 3, 2, 1]
    cnt_yes = len(set(lottos) & set(win_nums))
    cnt_0 = lottos.count(0)

    return [rank[cnt_yes + cnt_0], rank[cnt_yes]]


# 풀이 5
def solution5(lottos, win_nums):
    rank=[6, 6, 5, 4, 3, 2, 1]
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]