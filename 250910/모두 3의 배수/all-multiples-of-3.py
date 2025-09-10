is_true=[]
for _ in range(5):
    n = int(input())
    if n%3==0:
        is_true.append(True)
    
print(1) if sum(is_true)==5 else print(0)