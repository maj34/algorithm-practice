arr = list(map(int, input().split()))

tmp=[]
for i in arr:
    if i!=0:
        tmp.append(i)
    else:
        break

print(*[i//2 if i%2==0 else i+3 for i in tmp])