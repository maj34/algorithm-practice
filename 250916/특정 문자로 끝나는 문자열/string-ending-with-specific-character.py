arr = list(input() for _ in range(10))
char = input()

is_true=False
for i in arr:
    if i[-1] == char:
        print(i)
        is_true=True
    
if is_true==False:
    print("None")