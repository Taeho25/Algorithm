# [10] DFS - 음료수 얼려 먹기


# 1. N, M 입력 / 맵 정보 입력(2차원 리스트)
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 2. DFS로 특정 노드 방문 후 연결된 모든 노드 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True # 상하좌우 모두 거쳐오면 True
    
    return False # 이미 방문한 노드

# 3. 모든 노드에 음료수 채우기
result = 0
for node_x in range(n):
    for node_y in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(node_x, node_y) == True:
            result += 1

# 4. 결과 출력
print(result)