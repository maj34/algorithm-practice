n = int(input())
word = [input() for _ in range(n)]

for i in sorted(word):
    print(i)