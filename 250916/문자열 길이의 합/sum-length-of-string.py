N = int(input())
arr = list(input() for _ in range(N))

ssum=0
cnt=0
for i in arr:
    ssum += len(i)
    if i[0] == "a":
        cnt+=1
        
print(ssum, cnt)