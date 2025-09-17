a = input()
b = input()

a_num=""
b_num=""

for i in a:
    if 48 <= ord(i) <= 57:
        a_num+=i

for j in b:
    if 48 <= ord(j) <= 57:
        b_num+=j

print(int(a_num)+int(b_num))