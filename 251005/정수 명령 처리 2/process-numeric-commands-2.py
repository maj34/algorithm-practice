N = int(input())
A = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        A.append(int(line[1]))
    elif line[0] == "pop":
        print(A[0])
        A = A[1:]        
    elif line[0] == "size":
        print(len(A))
    elif line[0] == "empty":
        print("1" if len(A)==0 else "0")
    elif line[0] == "front":
        print(A[0])