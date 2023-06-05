# [42] 그래프 이론 - 도시 분할 계획


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


# 노드 개수, 간선 개수 입력 / 부모 테이블 초기화 / 간선 리스트, 최종비용 변수 선언
v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i
edges = []
result = 0

# 모든 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# 간선을 비용순으로 정렬
edges.sort()
last = 0  # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선

# 간선 하나씩 확인
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

# 결과 확인(가장 비용 큰 간선을 제외한 최종 비용)
print(result - last)