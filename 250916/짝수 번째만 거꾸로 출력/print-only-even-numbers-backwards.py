char = input()

char_even=[]
for i in range(len(char)):
    if i%2!=0:
        char_even.append(char[i])

for j in char_even[::-1]:
    print(j, end="")