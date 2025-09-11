N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    val_sum=0
    for i in range(a, b+1):
        if i%2==0:
            val_sum+=i
    print(val_sum)