A, B = map(int, input().split())

def divisor(N):
    numbers = set()
    for i in range(1, int(N**(1/2))+1):
        if N%i==0:
            numbers.add(i)
            numbers.add(N//i)
    return numbers

common_divisor = sorted(divisor(1920) & divisor(2880))

is_true=False
for i in range(A, B+1):
    if i in common_divisor:
        is_true=True

print(1) if is_true else print(0)