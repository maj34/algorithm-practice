N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 양방향 그래프 구성
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False for _ in range(N+1)]
cnt = 0

def dfs(si):
    global cnt
    visited[si] = True   
    for ni in graph[si]:
        if not visited[ni]:
            cnt += 1
            dfs(ni)

dfs(1)
print(cnt)