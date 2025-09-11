N = int(input())

tmp1 = 1
tmp2 = N
for i in range(2*N):
    if i%2==0:
        print("* "*tmp1)
        tmp1 += 1
    else:
        print("* "*tmp2)
        tmp2 -= 1