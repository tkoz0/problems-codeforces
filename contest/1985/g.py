t = int(input())
M = 10**9+7

def f(l,k,M):
    if k >= 10: return 0
    ret = 1 if l == 0 else pow(9//k+1,l,M)
    #print(f'f({l},{k},{M})={ret}')
    return ret

for _ in range(t):
    l,r,k = map(int,input().split())
    print((f(r,k,M)-f(l,k,M))%M)
