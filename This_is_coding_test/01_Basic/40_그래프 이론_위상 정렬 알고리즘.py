# [40] 그래프 이론 - 위상 정렬 알고리즘


# 풀이

from collections import deque

# 노드 개수, 간선 개수 입력 / 진입 차수 0으로 초기화
v, e = map(int, input().split())
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B로 이동 가능
    # 진입 차수 1 증가
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()  # 큐 기능

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

# 위상 정렬 수행
topology_sort()