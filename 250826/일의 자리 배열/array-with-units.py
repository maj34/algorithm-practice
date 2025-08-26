a, b = map(int, input().split())

num = [a, b]
for i in range(8):
    num.append((num[-1]+num[-2])%10) 

for j in num:
    print(j, end=" ")
