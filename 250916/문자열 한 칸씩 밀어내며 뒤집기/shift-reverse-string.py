char, Q = input().split()
queries = [int(input()) for _ in range(int(Q))]

for i in queries:
    if i == 1:
        char = char[1:] + char[:1]
        print(char)
    elif i == 2:
        char = char[-1:] + char[:-1]
        print(char)
    elif i == 3:
        char = char[::-1]
        print(char)