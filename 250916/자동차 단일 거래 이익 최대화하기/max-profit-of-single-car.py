n = int(input())
arr = list(map(int, input().split()))

max_arr=[]
min_arr=[]

for i in arr[arr.index(min(arr)):]:
    max_arr.append(i)
for j in arr[:arr.index(max(arr))]:
    min_arr.append(j)

if len(max_arr)==0 or len(min_arr)==0:
    profit = 0
elif max(max_arr)-min(arr) >= min(min_arr)-max(arr):
    profit = max(max_arr)-min(arr)
elif min(min_arr)-max(arr) > max(max_arr)-min(arr):
    profit = min(min_arr)-max(arr)
else:
    profit = 0

print(profit)