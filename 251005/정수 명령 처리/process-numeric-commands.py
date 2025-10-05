N = int(input())

value = []
for _ in range(N):
    line = input().split()
    if line[0] == "push":
        value.append(int(line[1]))
    elif line[0] == "size":
        print(len(value))
    elif line[0] == "empty":
        print("1" if len(value)==0 else "0")
    elif line[0] == "pop":
        print(value[-1])
        value = value[:-1]        
    elif line[0] == "top":
        print(value[-1])