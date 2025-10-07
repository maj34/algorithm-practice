N, K = map(int, input().split())

candy_dict = {}
for _ in range(N):
    c, p = map(int, input().split())
    candy_dict[p] = c

candy_dict = dict(sorted(candy_dict.items()))
candy_keys = candy_dict.keys()

max_candy = 0
for i in range(list(candy_keys)[0], list(candy_keys)[-1]+1):
    candy = 0
    for j in range(i-K, i+K+1):
        if j in candy_keys:
            candy += candy_dict[j]
    max_candy = max(max_candy, candy)
    
print(max_candy)