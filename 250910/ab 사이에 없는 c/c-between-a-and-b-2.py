a, b, c = map(int, input().split())

is_true=False
for i in range(a, b+1):
    if i%c==0:
        is_true=True

print("NO") if is_true else print("YES")