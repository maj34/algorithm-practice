n = int(input())
nums = list(map(int, input().split()))

for i in sorted(nums):
    print(i, end=" ")
print()
for i in sorted(nums, reverse=True):
    print(i, end=" ")