n = int(input())

for i in range(n): # 행
    for j in range(n): # 열
        if j%2==0:
            if i==0:
                print("* ", end="")
            else:
                print("  ", end="")
        else:
            if i<=j:
                print("* ", end="")
            else:
                print("  ", end="")
    print()