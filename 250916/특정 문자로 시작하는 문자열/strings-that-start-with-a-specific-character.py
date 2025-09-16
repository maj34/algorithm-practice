N = int(input())
arr = list(input() for i in range(N))
char = input()

cnt = 0
char_arr = []
for i in arr:
    if i[0] == char:
        cnt += 1
        char_arr.append(i)

char_len=0
for j in char_arr:
    char_len += len(j)

print(f"{cnt} {char_len/cnt:.2f}")