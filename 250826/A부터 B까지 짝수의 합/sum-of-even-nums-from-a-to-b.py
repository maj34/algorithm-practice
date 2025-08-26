A, B = map(int, input().split())

even = []
for i in range(A, B+1):
    if i % 2 == 0:
        even.append(i)

print(sum(even))