n = int(input())

ssum = 0
for _ in range(n):
    ssum += int(input())

print(str(ssum)[1:]+str(ssum)[:1])