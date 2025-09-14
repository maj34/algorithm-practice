N = int(input())
arr = list(map(int, input().split()))

cnt=0
for i in arr:
    if i==min(arr):
        cnt+=1

print(min(arr), end=" ")
print(cnt)