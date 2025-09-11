N = int(input())

for i in range(1, N+1):
    for j in range(1, N+1):
        if i <= j:
            if j==N:
                print(f"{i} * {j-i+1} = {i*(j-i+1)}")
            else:
                print(f"{i} * {j-i+1} = {i*(j-i+1)} / ", end="")