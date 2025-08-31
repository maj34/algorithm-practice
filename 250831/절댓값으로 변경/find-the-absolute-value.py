n = int(input())
arr = list(map(int, input().split()))

def absolute(arr):
    for i, num in enumerate(arr):
        arr[i] = abs(num)
    
absolute(arr)

for i in arr:
    print(i, end=" ")