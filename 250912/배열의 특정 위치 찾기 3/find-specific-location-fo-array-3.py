arr = list(map(int, input().split()))

for i in arr:
    arr.append(i)
    if i == 0:
        break

print(sum(arr[-2:-5:-1]))