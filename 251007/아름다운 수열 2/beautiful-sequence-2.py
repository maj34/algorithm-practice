N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from itertools import permutations
perm = []
for i in permutations(B, M):
    perm.append(list(i))

num = 0
for j in range(N-M+1):
    if A[j:j+M] in perm:
        num += 1

print(num)