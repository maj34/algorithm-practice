N = int(input())

num = 1
for i in range(N):
    for j in range(N):
        if i <= j:
            if num%10==0:
                num+=1
            print(num%10, end=" ")
            num+=1
        else:
            print(" ", end=" ")
    print()