from itertools import product

K, N = map(int, input().split())
lst = [i for i in range(1, K+1)]

perms = list(product(lst, repeat=N))
for p in perms:
    print(*p)