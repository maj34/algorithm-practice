n, char = input().split()

cnt = 0
for _ in range(int(n)):
    string = input()
    if string == char:
        cnt+=1

print(cnt)