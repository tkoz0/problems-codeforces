t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    r = x^y
    answer = 1
    while r & answer == 0:
        answer <<= 1
    print(answer)
