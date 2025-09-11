N = int(input())

for i in range(2*N+1):
    if i%2==0:
        print("* "*(2*N+1))
    else:
        print("*   "*(N+1))