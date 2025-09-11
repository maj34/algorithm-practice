start, end = map(int, input().split())

def divisor(n):
    numbers = set()
    for i in range(1, int(n**(1/2))+1):
        if n%i==0:
            numbers.add(i)
            numbers.add(n//i)
    return sorted(numbers)

cnt=0
for i in range(start, end+1):
    if sum(divisor(i)[:-1]) == divisor(i)[-1]:
        cnt+=1

print(cnt)