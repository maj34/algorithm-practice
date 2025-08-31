n, m = map(int, input().split())
A = list(map(int, input().split()))

def one_sum(m, A):
    ssum = 0
    while True:        
        if m == 1:
            ssum += A[m-1]
            break
        elif m%2 == 0:
            ssum += A[m-1]
            m //= 2
        else:
            ssum += A[m-1]
            m -= 1
    return ssum

print(one_sum(m, A))