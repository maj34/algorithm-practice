n = int(input())

# Please write your code here.
def square(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if num%10 == 0:
                num += 1
            print(num%10, end=" ")
            num += 1
        print()

square(n)