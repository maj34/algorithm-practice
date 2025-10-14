n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 양방향 그래프 구성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]
cnt = 0

def dfs(v):
    global cnt
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            cnt += 1
            dfs(next_v)

dfs(1)
print(cnt)