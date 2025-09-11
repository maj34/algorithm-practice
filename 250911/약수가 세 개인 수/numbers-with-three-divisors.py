start, end = map(int, input().split())

def divisor(n):
    numbers = set()
    for i in range(1, int(n**(1/2))+1):
        if n%i==0:
            numbers.add(i)
            numbers.add(n//i)
    return len(numbers)

cnt=0
for j in range(start, end+1):
    if divisor(j) == 3:
        cnt+=1

print(cnt)