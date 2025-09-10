A, B = map(int, input().split())

prod=1
for i in range(A, B+1):
    prod*=i

print(prod)