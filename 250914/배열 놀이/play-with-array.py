N, Q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(Q):
    rule = list(map(int, input().split()))
    if rule[0]==1:
        print(arr[rule[1]-1])
    elif rule[0]==2:
        if rule[1] in arr:
            print(arr.index(rule[1])+1)
        else:
            print(0)
    elif rule[0]==3:
        print(*arr[rule[1]-1:rule[2]])