N = int(input())

if N % 2 == 1 and N % 3 == 0:
    print("true")
elif N % 2 == 0 and N % 5 == 0:
    print("true")
else: 
    print("false")