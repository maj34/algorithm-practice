from collections import deque

N = int(input())

# 1부터 시작해서 
def bfs(N):
    q = deque()
    visited = [False for _ in range(1, 3000001)]

    q.append((1, 0))
    visited[1] = True

    while q:
        cnum, dist = q.popleft()
        
        # 종료조건
        if cnum == N:
            return dist
        
        for dnum in range(4):
            if dnum == 0:
                nnum = cnum + 1
                if 1<=nnum<1000000 and not visited[nnum]:
                    q.append((nnum, dist+1))
                    visited[nnum] = True
            elif dnum == 1:
                nnum = cnum - 1
                if 1<=nnum<1000000 and not visited[nnum]:
                    q.append((nnum, dist+1))
                    visited[nnum] = True
            elif dnum == 2:
                nnum = cnum * 2
                if 1<=nnum<1000000 and not visited[nnum]:
                    q.append((nnum, dist+1))
                    visited[nnum] = True
            elif dnum == 3:
                nnum = cnum * 3
                if 1<=nnum<1000000 and not visited[nnum]:
                    q.append((nnum, dist+1))
                    visited[nnum] = True

print(bfs(N))