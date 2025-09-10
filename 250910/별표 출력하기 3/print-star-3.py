N = int(input())

tmp = 0
for i in range(2*N-1, 0, -2):
    print("  "*tmp, end="")
    print("* "*i)
    tmp+=1