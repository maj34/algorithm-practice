n = int(input())
char = list(input().split())

num=""
for i in char:
    num+=i

cnt=0
for j in num:
    if cnt == 5:
        print()
        print(j, end="")
        cnt=1
    else:
        print(j, end="")
        cnt+=1