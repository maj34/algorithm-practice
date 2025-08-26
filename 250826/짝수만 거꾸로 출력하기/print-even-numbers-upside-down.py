N = int(input())
num_list = list(input().split())

even_list = []
for i in num_list:
    if int(i) % 2 == 0:
        even_list.append(i)
    else:
        continue

for j in even_list[::-1]:
    print(j, end=" ")