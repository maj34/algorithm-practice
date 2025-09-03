n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)

max_num = 0
for i in range(n):
    ssum = sorted_nums[n-i] + sorted_nums[n+i-1]
    if max_num < ssum:
        max_num = ssum
        
print(max_num)

