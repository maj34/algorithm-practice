arr = map(int, input().split())

less = []
more = []

for i in arr:
    if i<500:
        less.append(i)
    elif i>500:
        more.append(i)

print(max(less), min(more))