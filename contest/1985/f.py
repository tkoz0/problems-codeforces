# combine attacks with same cooldown
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

def dmg(a,c,n,turns):
    return sum(a[i]*(turns//c[i]) for i in range(n))

# binary search method
t = int(input())
for _ in range(t):
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    # the hashing bullshit again, dont use the fixac thing
    #a,c = fixac(a,c)
    #n = len(a)
    h -= sum(a)
    # count additional turns needed
    lo = 0
    hi = 1
    while h - dmg(a,c,n,hi) > 0:
        hi *= 2
    while lo != hi:
        m = (lo+hi)//2
        d = dmg(a,c,n,m)
        if h - d > 0:
            lo = m+1
        else:
            hi = m
    print(lo+1)
