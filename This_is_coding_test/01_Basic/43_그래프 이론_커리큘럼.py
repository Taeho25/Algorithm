# [43] 그래프 이론 - 커리큘럼


# 풀이

from collections import deque
import copy

# 노드 개수 입력 / 진입 차수 0으로 초기화 / 연결 리스트 초기화 / 강의 시간 초기화
v = int(input())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보 입력
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 시간 정보
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)  # 알고리즘 수행 결과를 담을 리스트
    q = deque()  # 큐 기능

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i], end=' ')

# 위상 정렬 수행
topology_sort()