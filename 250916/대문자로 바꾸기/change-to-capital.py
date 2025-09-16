arr = [
    list(input().split())
    for _ in range(5)
]

for i in arr:
    for j in i:
        print(j.upper(), end=" ")
    print()