n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

t_list = []
for i in sorted(str):
    if i.startswith(t):
        t_list.append(i)

print(t_list[k-1])