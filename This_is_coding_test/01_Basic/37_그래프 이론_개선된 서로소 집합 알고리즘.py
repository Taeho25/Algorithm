# [37] 그래프 이론 - 개선된 서로소 집합 알고리즘


# 풀이

# 특정 원소가 속한 집합 찾기(경로 압축 기법 적용)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
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


# 노드 개수(v), 간선(union 연산) 개수(e) 입력 / 부모 테이블 초기화
v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')