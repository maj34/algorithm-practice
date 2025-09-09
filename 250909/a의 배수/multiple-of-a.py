N, a = map(int, input().split())

i = 1
while i <= N:
    if i % a==0:
        print(1)
    else:
        print(0)
    i+=1