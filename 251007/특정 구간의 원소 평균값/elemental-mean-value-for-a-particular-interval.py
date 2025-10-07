n = int(input())
arr = list(map(int, input().split()))

same_num = 0
for i in range(n):
    for j in range(i, n):
        ssum, num = 0, 0
        for k in range(i, j+1):
            ssum += arr[k]
            num += 1
        mean = ssum / num
        for l in range(i, j+1):
            if mean == arr[l]:
                same_num += 1
                break

print(same_num)