A, B = map(int, input().split())

val_sum = 0
if A >= B:
    for i in range(B, A+1):
        if i%5==0:
            val_sum+=i
else:
    for i in range(A, B+1):
        if i%5==0:
            val_sum+=i

print(val_sum)