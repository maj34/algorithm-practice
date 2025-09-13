arr = list(map(int, input().split()))

arr1 = [i for i in arr if i!=0]
print(*[i//2 if i%2==0 else i+3 for i in arr1])