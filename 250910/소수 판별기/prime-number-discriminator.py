N = int(input())

def divisor(N):
    numbers = set()
    for i in range(1, int(N**(1/2))+1):
        if N%i==0:
            numbers.add(i)
            numbers.add(N//i)
    return numbers

print("P") if len(divisor(N))==2 else print("C")