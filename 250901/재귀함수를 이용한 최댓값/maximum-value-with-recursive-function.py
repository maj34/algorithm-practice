n = int(input())
arr = list(map(int, input().split()))

def maximum(n):
    if n == 0:
        return arr[0]
    return max(maximum(n-1), arr[n])

print(maximum(n-1))