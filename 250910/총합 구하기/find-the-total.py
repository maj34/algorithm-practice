A, B = map(int, input().split())

val_sum=0
for i in range(A, B+1):
    if i%6==0 and i%8!=0:
        val_sum+=i

print(val_sum)