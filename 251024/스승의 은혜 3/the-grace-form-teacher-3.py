N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

max_cnt = 0
for i in range(N):
    temp_budget = B - (P[i] // 2 + S[i])
    cnt = 1
    costs = []
    for j in range(N):
        if i != j:
            costs.append(P[j] + S[j])
    costs.sort()
    for cost in costs:
        if temp_budget >= cost:
            temp_budget -= cost
            cnt += 1
        else:
            break
    max_cnt = max(max_cnt, cnt)

print(max_cnt)