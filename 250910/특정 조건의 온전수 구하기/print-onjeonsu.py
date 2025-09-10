N = int(input())

for i in range(1, N+1):
    if i%2==0:
        continue
    elif i%10==5:
        continue
    elif i%3==0 and i%9!=0:
        continue
    else:
        print(i, end=" ")