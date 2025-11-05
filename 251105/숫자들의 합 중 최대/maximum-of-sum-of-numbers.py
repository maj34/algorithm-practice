X, Y = map(int, input().split())

max_sum = 0
for i in range(X, Y+1):
    ssum = 0
    for j in range(len(str(i))):
        ssum += int(str(i)[j])
    max_sum = max(max_sum, ssum)

print(max_sum)