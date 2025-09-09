C, N = input().split()

if C=="A":
    for i in range(1, int(N)+1):
        print(i, end=" ")
elif C=="D":
    for j in range(int(N), 0, -1):
        print(j, end=" ")