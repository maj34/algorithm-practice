n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(sorted(nums)[k-1])