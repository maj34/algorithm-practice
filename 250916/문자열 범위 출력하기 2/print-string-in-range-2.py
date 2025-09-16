char = input()
num = int(input())

char_num = char[-num:]

for i in char_num[::-1]:
    print(i, end="")