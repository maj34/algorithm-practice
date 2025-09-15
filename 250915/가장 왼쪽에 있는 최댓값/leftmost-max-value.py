n = int(input())
arr = list(map(int, input().split()))

idx=-1
while idx!=0:
    idx = arr.index(max(arr))
    arr = arr[:idx]
    print(idx+1, end=" ")