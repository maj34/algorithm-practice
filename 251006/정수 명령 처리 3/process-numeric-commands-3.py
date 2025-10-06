n = int(input())
num = []

for _ in range(n):
    line = input().split()
    if line[0] == "push_front":
        num = [int(line[1])] + num
    elif line[0] == "push_back":
        num.append(int(line[1]))
    elif line[0] == "pop_front":
        print(num[0])
        num = num[1:]
    elif line[0] == "pop_back":
        print(num[-1])
        num = num[:-1]
    elif line[0] == "size":
        print(len(num))
    elif line[0] == "empty":
        print("1" if len(num) == 0 else "0")
    elif line[0] == "front":
        print(num[0])
    elif line[0] == "back":
        print(num[-1])