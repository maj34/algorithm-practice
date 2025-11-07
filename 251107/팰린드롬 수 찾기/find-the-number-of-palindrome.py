X, Y = map(int, input().split())

print(sum(1 for i in range(X, Y+1) if str(i) == str(i)[::-1]))