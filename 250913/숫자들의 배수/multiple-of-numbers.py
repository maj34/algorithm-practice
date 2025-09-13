n = int(input())

five=0
prod=0
while True:
    prod+=1
    print(n*prod, end=" ")
    if (n*prod%5)==0:
        five+=1
        if five==2:
            break