n, m = map(int, input().split())
A = list(map(int, input().split()))

def one_sum(n, m, A):
    ssum = 0
    while m != 1:
        ssum += A[int(m)-1]
        if m%2 == 0:
            m /= 2
        else:
            ssum += A[int(m)]
            m -= 1
    ssum += A[0]
    return ssum

print(one_sum(n, m, A))