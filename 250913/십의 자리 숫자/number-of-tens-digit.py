arr = list(map(int, input().split()))

result=[0]*10
for i in arr:
    if i==0:
        break
    else:
        result[i//10] += 1

for j in range(len(result)-1):
    print(f"{j+1} - {result[j+1]}")