arr = list(map(int, input().split()))

result=[]
for i in arr:
    if i==999 or i==-999:
        break
    result.append(i)

print(max(result), min(result))