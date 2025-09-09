N = int(input())

val_sum=0
for _ in range(N):
    a = int(input())
    if a%2!=0 and a%3==0:
        val_sum+=a

print(val_sum)