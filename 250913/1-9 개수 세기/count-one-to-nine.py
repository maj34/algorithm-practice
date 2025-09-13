N = int(input())
arr = list(map(int, input().split()))

ten=[0]*9
for i in arr:
    ten[i-1]+=1

for j in ten:
    print(j)