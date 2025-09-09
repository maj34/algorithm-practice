val_sum = 0
val_num = 0
for _ in range(10):
    a = int(input())
    if 0<=a<=200:
        val_sum+=a
        val_num+=1

print(f"{val_sum} {val_sum/val_num:.1f}")
