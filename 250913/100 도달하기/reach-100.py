N = int(input())

arr = [1, N]
while True:
    arr.append(arr[-2]+arr[-1])
    if arr[-2]+arr[-1]>100:
        arr.append(arr[-2]+arr[-1])
        break

print(*arr)