n = int(input())
arr = list(map(int, input().split()))

minimum=min(arr)
maximum=max(arr)
max_arr=[]
min_arr=[]

# 최솟값을 기준으로 최댓값 찾기
for i in arr[arr.index(minimum):]:
    max_arr.append(i)
right_max = max(max_arr)

# 최댓값을 기준으로 최솟값 찾기
for j in arr[:arr.index(maximum)+1]:
    min_arr.append(j)
left_min = min(min_arr)

profit = max(right_max - minimum, left_min - maximum)
print(profit)