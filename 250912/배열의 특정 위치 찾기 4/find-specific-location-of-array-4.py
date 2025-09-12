arr = list(map(int, input().split()))

arr1=[]
for i in arr:
    if i!=0:
        if i%2==0:
            arr1.append(i)
    else:
        break

print(len(arr1), sum(arr1))