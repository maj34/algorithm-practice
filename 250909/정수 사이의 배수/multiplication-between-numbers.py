A, B = map(int, input().split())

val_sum = 0
num = 0
for i in range(A, B+1):
    if i%5==0 or i%7==0:
        val_sum+=i
        num+=1

print(f"{val_sum} {val_sum/num:.1f}")