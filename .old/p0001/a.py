
n, m, a = tuple(map(int,input().split(' ')))
for v in (n,m,a): assert 1 <= v <= 10**9
print(((n+a-1)//a)*((m+a-1)//a))
