N = int(input().strip())
lines = [tuple(map(int, input().split())) for _ in range(N)]  # (x1, x2)

ans = 0
for i in range(N):
    x1i, x2i = lines[i]
    ok = True
    for j in range(N):
        if i == j:
            continue
        x1j, x2j = lines[j]
        # 순서가 반대면 교차
        if (x1i - x1j) * (x2i - x2j) < 0:
            ok = False
            break
    if ok:
        ans += 1

print(ans)