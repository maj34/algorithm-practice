arr = list(map(int, input().split()))

tmp=[]
for i in range(len(arr)):
    tmp.append(arr[i])
    if arr[i]%3==0:
        break

print(tmp[-2])