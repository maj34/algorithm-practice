string = input()
char = input()

cnt = 0
for i in range(len(string)-1):
    if string[i:i+2] == char:
        cnt += 1

print(cnt)