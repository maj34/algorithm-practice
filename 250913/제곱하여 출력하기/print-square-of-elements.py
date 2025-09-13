N = int(input())
arr = list(map(int, input().split()))

print(*[i**2 for i in arr])