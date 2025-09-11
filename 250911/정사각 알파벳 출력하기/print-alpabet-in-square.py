N = int(input())

num = 0
for i in range(N):
    for j in range(N):
        print(chr(ord("A")+num), end="")
        num+=1
    print()