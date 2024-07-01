
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    longest = 0
    answer = (0,0)
    for i in range(n):
        i1 = grid[i].find('#')
        if i1 == -1: continue
        i2 = grid[i][::-1].find('#')
        l = len(grid[i]) - i1 - i2
        if l < longest: continue
        j = i1 + l//2
        longest = l
        answer = (i+1,j+1)
    print(answer[0],answer[1])
