n = int(input())
arr = list(map(int, input().split()))

def solution(arr):
    for i, num in enumerate(arr):
        if num % 2 == 0:
            arr[i] = int(num/2)
    for j in arr:
        print(j, end=" ")

solution(arr)