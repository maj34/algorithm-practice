a, b = map(int, input().split())

def intact(n):
    if n % 2 == 0:
        return False
    elif n % 10 == 5:
        return False
    elif n % 3 == 0 and n % 9 != 0:
        return False
    else:
        return True
    
num = 0
for i in range(a, b+1):
    if intact(i) == True:
        num += 1
    else:
        continue

print(num)
