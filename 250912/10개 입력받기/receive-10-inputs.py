arr = list(map(int, input().split()))

val_sum=0
num=0
for i in arr:
    if i!=0:
        val_sum+=i
        num+=1
    else:
        break

print(f"{val_sum} {val_sum/num:.1f}")