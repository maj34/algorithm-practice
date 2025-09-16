arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

ssum=0
for i in range(4):
    for j in range(4):
        if j <= i:
            ssum+=arr[i][j]
print(ssum)