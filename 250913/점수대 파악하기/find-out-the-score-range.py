arr = list(map(int, input().split()))

result=[0]*10
for i in arr:
    if i==0:
        break
    elif i==100:
        result[-1] += 1
    else:
        result[i//10-1] += 1

idx=100
for cnt in result[::-1]:
    print(f"{idx} - {cnt}")
    idx-=10