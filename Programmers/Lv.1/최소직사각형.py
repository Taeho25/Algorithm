'''Lv.1 최소직사각형'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/86491


# 풀이 1
def solution(sizes):
    ws = []
    hs = []
    for idx in range(len(sizes)):
        if sizes[idx][0] > sizes[idx][1]:
            ws.append(sizes[idx][0])
            hs.append(sizes[idx][1])
        else:
            ws.append(sizes[idx][1])
            hs.append(sizes[idx][0])
    max_w = max(ws)
    max_h = max(hs)
    answer = max_w * max_h
    return answer

  
# 풀이 2
def solution2(sizes):
    ws, hs = [], []
    for w, h in sizes:
        if w < h: w, h = h, w
        ws.append(w)
        hs.append(h)
    return max(ws) * max(hs)


# 풀이 3
def solution3(sizes):
    w = max(max(x) for x in sizes)  # 큰 것들 중에 제일 큰 것
    h = max(min(x) for x in sizes)  # 작은 것들 중에 제일 큰 것
    return w * h


# 풀이 4
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)  # sum()의 가능성
