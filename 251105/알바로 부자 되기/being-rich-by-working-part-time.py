import bisect

N = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(N)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

jobs.sort(key=lambda x: x[1])
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

dp = [0] * (N + 1)
ends = [job[1] for job in jobs]

for i in range(1, N + 1):
    start_i, end_i, profit_i = jobs[i - 1]

    j = bisect.bisect_right(ends, start_i - 1)
    dp[i] = max(dp[i - 1], dp[j] + profit_i)

print(dp[N])