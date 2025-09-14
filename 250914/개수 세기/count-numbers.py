N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt=0
for i in arr:
    if i==M:
        cnt+=1

print(cnt)