n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

lines.sort(key=lambda x:x[1])

cnt, end = 0, 0
for l, r in lines:
    if l > end:
        cnt += 1
        end = r

print(cnt)