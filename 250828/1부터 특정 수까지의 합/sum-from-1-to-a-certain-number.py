n = int(input())

# Please write your code here.
def solution(n):
    ssum = 0
    for i in range(1, n+1):
        ssum += i
    answer = int(ssum/10)
    return answer

print(solution(n))

