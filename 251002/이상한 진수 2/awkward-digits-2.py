a = input()

for idx, num in enumerate(a):
    if num == '0':
        a = a[:idx] + "1" + a[idx+1:]
        print(int(a, 2))
        break
    if set(a) == {"1"}:
        a = a[:-1] + "0"
        print(int(a, 2))