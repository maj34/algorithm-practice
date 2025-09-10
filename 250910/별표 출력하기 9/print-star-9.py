N = int(input())

tmp = N-1
for i in range(1, 2*N, 2):
    print("  "*tmp, end="")
    print("* "*i)
    tmp-=1