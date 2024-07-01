t = int(input())
for _ in range(t):
    n = int(input())
    maxs = 0
    maxx = 0
    for x in range(2,n+1):
        L = n//x
        S = x*L*(L+1)//2
        if S > maxs:
            maxs = S
            maxx = x
    print(maxx)
