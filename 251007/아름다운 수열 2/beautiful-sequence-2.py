from itertools import permutations

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

num = 0
for i in range(N-M+1):
    sub = A[i:i+M]
    for j in permutations(B, M):
        if list(j) == sub:
            num += 1
            break

print(num)