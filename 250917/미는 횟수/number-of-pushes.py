a = input()
b = input()

cnt=1
for _ in range(len(a)-1):
    a = a[-1]+a[:-1]
    if a == b:
        break
    else:
        cnt+=1

print(cnt) if cnt < (len(a)-1) else print(-1)