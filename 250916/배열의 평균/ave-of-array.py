arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 가로 평균
for i in arr:
    print(f"{sum(i)/4:.1f}", end=" ")
print()

# 세로 평균
ssum1 = 0
ssum2 = 0
ssum3 = 0
ssum4 = 0
for i in arr:
    ssum1 += i[0]
    ssum2 += i[1]
    ssum3 += i[2]
    ssum4 += i[3]
print(f"{ssum1/2:.1f} {ssum2/2:.1f} {ssum3/2:.1f} {ssum4/2:.1f}")

# 전체 평균
print(f"{(ssum1+ssum2+ssum3+ssum4)/8:.1f}")