a, b = map(int, input().split())

if a>=90 and b>=95:
    print(100000)
elif a>=90 and b>=90:
    print(50000)
else:
    print(0)