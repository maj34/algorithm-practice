N = int(input())

val_sum=0
for i in range(1, 101):
    val_sum+=i
    if val_sum >= N:
        print(i)
        break