A, B = map(int, input().split())

for i in range(1, 10):
    for j in range(B, A-1, -2):
        if j > A:
           print(f"{j} * {i} = {i*j} / ", end="")
        else:
            print(f"{j} * {i} = {i*j}")