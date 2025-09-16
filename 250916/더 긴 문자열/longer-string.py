a, b = input().split()

if len(a) > len(b):
    print(a, len(a))
elif len(a) < len(b):
    print(b, len(b))
else:
    print("same")
