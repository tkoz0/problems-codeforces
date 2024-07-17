t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = max(a[0],a[1])
    for i in range(1,n):
        k = min(k,max(a[i-1],a[i]))
    print(k-1)
