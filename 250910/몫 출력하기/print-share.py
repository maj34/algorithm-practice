num=0
while True:
    n = int(input())
    if n%2!=0:
        continue
    else:
        print(n//2)
        num+=1
        if num==3:
            break