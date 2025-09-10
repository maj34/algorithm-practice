N = int(input())

def divisor(N):
    nums = set()
    for i in range(1, int(N**(1/2))+1):
        if N % i == 0:
            nums.add(i)
            nums.add(N//i)
    return sorted(nums)

if sum(divisor(N)[:-1]) == divisor(N)[-1]:
    print("P")
else:
    print("N")