num=0
char_list=[]
while True:
    char = input()
    if char == "0":
        break
    else:
        num += 1
        if num%2 != 0:
            char_list.append(char)

print(num)
for i in char_list:
    print(i)