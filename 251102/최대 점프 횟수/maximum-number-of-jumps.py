N = int(input())
lst = list(map(int, input().split()))

dp = [-1] * N

def dfs(i):
    if dp[i] != -1:
        return dp[i]
    
    # 현재 위치에서 더 이상 앞으로 못 가면 0
    best = 0
    max_step = lst[i]

    for step in range(1, max_step+1):
        ni = i + step
        if ni >= N:
            break
        best = max(best, dfs(ni)+1) # ni에서 더 이어갈 수 있는 최댓값을 더함
    dp[i] = best
    return dp[i]

print(dfs(0))