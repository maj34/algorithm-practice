N = int(input())

for i in range(N, 0, -1):
    for j in range(N, 0, -1):
        if i >= j: 
            print(j, end=" ")
        else: 
            print(" ", end=" ")
    print()