N = int(input())

for _ in range(N):
    num = int(input())
    cnt = 0
    while num != 1:
        if num%2==0:
            num//=2
            cnt+=1
        else:
            num=num*3+1
            cnt+=1
    print(cnt)