arr = list(map(int, input().split()))

val_sum=0
for i in arr:
    if i%2!=0:
        val_sum+=arr[i]

print(val_sum, end=" ")

idx=2
val_sum=0
num=0
for j in arr:
    if idx <= len(arr)-1:
        val_sum+=arr[idx] 
        idx+=3
        num+=1

print(f"{val_sum/num:.1f}")