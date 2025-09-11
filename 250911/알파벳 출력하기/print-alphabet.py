N = int(input())

num=0
for i in range(N):
    for j in range(N):
        if i >= j:
            print(chr(ord("A")+num), end="")
            if (ord("A")+num)==90:
                num-=26
            num+=1
    print()