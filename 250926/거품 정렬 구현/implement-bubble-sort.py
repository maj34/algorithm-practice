n = int(input())
arr = list(map(int, input().split()))

is_sorted=False
while not is_sorted:
    is_sorted=True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            is_sorted=False

for i in arr:
    print(i, end=" ")