A = int(input())

for i in range(1, A+1):
    if i%2==0 and i%4!=0:
        continue
    elif (i//8)%2==0:
        continue
    elif (i%7)<4:   
        continue
    else:
        print(i, end=" ")