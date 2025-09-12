arr = list(map(int, input().split()))

sum_val=0
num=0
for i in arr:
    if i<250:
        sum_val+=i
        num+=1
    else:
        break

print(f"{sum_val} {sum_val/num:.1f}")