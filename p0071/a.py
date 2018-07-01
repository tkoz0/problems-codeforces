n = int(input())
assert 1 <= n <= 100
for z in range(n):
    w = input()
    assert 1 <= len(w) <= 100
    if len(w) <= 10: print(w)
    else: print(w[0],len(w)-2,w[-1],sep='')
