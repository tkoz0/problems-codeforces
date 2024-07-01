# this is a simple change from h1 that is wrong

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    grid = [input() for _ in range(n)]
    v = [[False]*m for _ in range(n)]
    rowdots = [0]*n
    coldots = [0]*m
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                rowdots[i] += 1
                coldots[j] += 1
    rowinfo = [0]*n
    colinfo = [0]*m
    compsizeinfo = [[0]*m for _ in range(n)]
    def bfs(i,j): # called once per component
        if v[i][j] or grid[i][j] == '.':
            return
        v[i][j] = True
        qall = [(i,j)]
        q = [(i,j)]
        compsize = 1
        rmin,rmax = i,i
        cmin,cmax = j,j
        while q:
            q2 = []
            for ii,jj in q:
                for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    iii,jjj = ii+di,jj+dj
                    if 0 <= iii < n and 0 <= jjj < m \
                            and grid[iii][jjj] == '#' \
                            and not v[iii][jjj]:
                        q2.append((iii,jjj))
                        v[iii][jjj] = True
                        rmin = min(rmin,iii)
                        rmax = max(rmax,iii)
                        cmin = min(cmin,jjj)
                        cmax = max(cmax,jjj)
                        compsize += 1
            q = q2
            qall += q2
        if rmin > 0: rmin -= 1
        if rmax < n-1: rmax += 1
        if cmin > 0: cmin -= 1
        if cmax < m-1: cmax += 1
        for ii in range(rmin,rmax+1):
            rowinfo[ii] += compsize
        for jj in range(cmin,cmax+1):
            colinfo[jj] += compsize
        for ii,jj in qall:
            compsizeinfo[ii][jj] = compsize
    for i in range(n):
        for j in range(m):
            bfs(i,j)
    answer = 0
    for i in range(n):
        for j in range(m):
            z = rowinfo[i] + colinfo[j] + rowdots[i] + coldots[j]
            if grid[i][j] == '.': z -= 1
            else: z -= compsizeinfo[i][j]
            answer = max(answer,z)
    print(answer)
