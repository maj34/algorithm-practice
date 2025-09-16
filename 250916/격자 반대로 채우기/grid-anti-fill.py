N = int(input())
arr = [[0]*N for _ in range(N)]

num = N*N
if N%2 == 0:
    for i in range(N):
        if i%2==0:
            for j in range(N-1, -1, -1):
                arr[j][i] = num
                num -= 1
        else:
            for k in range(N):
                arr[k][i] = num
                num -= 1
else:
    for i in range(N):
        if i%2!=0:
            for j in range(N-1, -1, -1):
                arr[j][i] = num
                num -= 1
        else:
            for k in range(N):
                arr[k][i] = num
                num -= 1

for l in arr:
    for o in l:
        print(o, end=" ")
    print()