from collections import Counter

n = int(input())
people = [tuple(input().split()) for _ in range(n)]
sorted_people = sorted(people, key=lambda x: int(x[0]))

max_size = 0
for i in range(n):
    stack = []
    size = 0
    for j in range(i, n):        
        stack.append(sorted_people[j][1])
        if len(set(stack)) == 1 or len(set(Counter(stack).values())) == 1:
            size = int(sorted_people[j][0]) - int(sorted_people[i][0])
        max_size = max(max_size, size)

print(max_size)