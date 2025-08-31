n = int(input())
arr = list(map(int, input().split()))

def absolute(arr):
    for i, num in enumerate(arr):
        arr[i] = abs(num)
    return arr

for i in absolute(arr):
    print(i, end=" ")