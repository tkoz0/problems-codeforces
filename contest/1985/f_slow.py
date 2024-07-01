# combine attacks of same cooldown into one
def fixac(a,c):
    m = dict() # cooldown -> sum attacks
    for i in range(len(a)):
        if c[i] not in m:
            m[c[i]] = 0
        m[c[i]] += a[i]
    ra,rc = [],[]
    for k in m:
        ra.append(m[k])
        rc.append(k)
    return ra,rc

t = int(input())
for _ in range(t):
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    a,c = fixac(a,c)
    n = len(a)
    wait = c[:]
    h -= sum(a) # handle first turn
    turns = 1
    while h > 0:
        waitmin = min(wait)
        wait = [w-waitmin for w in wait]
        turns += waitmin
        for i in range(n):
            if wait[i] == 0:
                h -= a[i]
                wait[i] = c[i]
    print(turns)
