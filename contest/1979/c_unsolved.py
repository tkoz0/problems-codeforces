t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int,input().split()))
    x = [1]*n
    sumx = n
    solved = False
    while True:
        for i in range(n):
            if k[i]*x[i] <= sumx:
                xi = 1 + sumx//k[i]
                sumx += xi - x[i]
                x[i] = xi
        if all(k[i]*x[i] > sumx for i in range(n)):
            print(' '.join(map(str,x)))
            solved = True
            break
        if max(x) > 10**9:
            break
    if not solved:
        print(-1)
