N = int(input())
arr = list(map(int, input().split()))

reversed_arr=[]
for i in arr:
    if i%2==0:
        reversed_arr.append(i)

print(*reversed_arr[::-1])