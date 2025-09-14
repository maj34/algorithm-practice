N = int(input())
arr = list(map(int, input().split()))

print(max(arr), end=" ")
arr.remove(max(arr))
print(max(arr))