# [41] 그래프 이론 - 팀 결성


# 풀이

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 입력
n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(0, n + 1):
    parent[i] = i

# 각 연산 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:  # 팀 합치기 연산
        union_parent(parent, a, b)
    elif oper == 1:  # 같은 팀 여부 확인 연산
        if find_parent(parent, a) == find_parent(parent, b):
            print("Yes")
        else:
            print("No")