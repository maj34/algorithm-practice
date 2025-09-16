A = input()

char=""
cnt=1
for i in range(1, len(A)):
    if A[i] == A[i-1]:
        cnt+=1
    else:
        char+=A[i-1]
        char+=str(cnt)
        cnt=1

char+=A[len(A)-1]
char+=str(cnt)

print(len(char))
print(char)