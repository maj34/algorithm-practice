N = int(input())

num=0
while N != 1:
    if N%2==0:
        N//=2
    else:
        N=N*3+1
    num+=1
    
print(num)