a, b = map(int, input().split())

# Please write your code here.
def is_three(n):
    for i in range(len(str(n))): 
        if str(n)[i] in ['3', '6', '9']:
            return True
    if n % 3 == 0:
        return True

def solution(a, b):
    num = 0
    for j in range(a, b+1):
        if is_three(j) == True:
            num += 1
    return num

print(solution(a, b))