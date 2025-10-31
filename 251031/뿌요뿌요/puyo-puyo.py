N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def dfs(si, sj, num, visited):
    cnt = 1
    visited[si][sj] = True

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and grid[ni][nj] == num:   
            cnt += dfs(ni, nj, num, visited)
    return cnt

max_num = max(max(n) for n in grid)

num_cnt = {}
for num in range(1, max_num+1):
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if 0<=i<N and 0<=j<N and not visited[i][j] and grid[i][j] == num:
                count = dfs(i, j, num, visited)
                if num in num_cnt:
                    num_cnt[num].append(count)
                else:
                    num_cnt[num] = [count]

over_num, max_sum = 0, 0
for k, v in num_cnt.items():
    if any(block >= 4 for block in v):  # 각 블록 중 4 이상인 것만 체크
        over_num += sum(1 for block in v if block >= 4)  # 블록 개수를 정확히 세기
    max_sum = max(max_sum, max(v))

print(over_num, max_sum)