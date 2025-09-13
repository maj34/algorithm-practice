arr = map(int, input().split())

result=[0]*6
for i in arr:
    result[i-1]+=1

for j in range(len(result)):
    print(f"{j+1} - {result[j]}")