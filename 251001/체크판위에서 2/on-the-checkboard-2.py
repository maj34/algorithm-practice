R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

cnt = []
for i in range(R):
    for j in range(C):
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                if grid[i][j] != grid[k][l]:
                    for a in range(k+1, R-1):
                        for b in range(l+1, C-1):
                            if grid[k][l] != grid[a][b]:
                                cnt.append(str(k)+str(l)+str(a)+str(b))

print(len(set(cnt)))