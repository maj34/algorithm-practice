N = int(input())
arr = list(map(int, input().split()))

from collections import Counter

results=[]
for k,v in Counter(arr).items():
    if v==1:
        results.append(k)

if len(results)==0:
    print(-1)
else:
    print(max(results))