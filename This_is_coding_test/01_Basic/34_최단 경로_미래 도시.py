# [34] 최단 경로 - 미래 도시


# 풀이
INF = int(1e9) # 무한 의미(10억)

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for me in range(1, n + 1):
    graph[me][me] = 0

# 각 간선에 대한 정보 입력, 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print("-1")
else:
    print(distance)