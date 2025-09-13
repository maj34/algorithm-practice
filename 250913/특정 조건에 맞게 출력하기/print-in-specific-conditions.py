arr = list(map(int, input().split()))

result = []
for i in arr:
    if i == 0:
        break
    result.append(i)

print(*[i//2 if i%2==0 else i+3 for i in result])