from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

target = Counter(B)

num = 0
for i in range(N-M+1):
    sub = A[i:i+M]
    if Counter(sub) == target:
        num += 1

print(num)