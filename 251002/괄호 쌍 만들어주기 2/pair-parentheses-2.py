a = input()

cnt = 0
for i in range(len(a)):
    for j in range(2, len(a)-(i+2)+1):
        if a[i:i+2] == "((" and a[i+j:i+j+2] == "))":
            cnt += 1

print(cnt)