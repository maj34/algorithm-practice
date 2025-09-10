N = int(input())

num=0
for i in range(1, N+1):
    N = N//i
    if N <= 1:
        num+=1
        print(num)
        break
    else:
        num+=1
    