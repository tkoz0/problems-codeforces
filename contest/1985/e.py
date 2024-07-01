t = int(input())
for _ in range(t):
    x,y,z,k = map(int,input().split())
    sx,sy,sz = 0,0,0 # sx*sy*sz = k
    answer = 0
    for sx in range(1,x+1):
        if k % sx == 0:
            a = k // sx
            for sy in range(1,a+1):
                if sy*sy > a or sy > y: break
                if a % sy == 0:
                    sz = a // sy
                    if sz <= z:
                        answer = max(answer,(1+x-sx)*(1+y-sy)*(1+z-sz))
                        '''
                        IGNORE THIS BULLSHIT FOR NOW
                        if sx <= x and sy <= z and sz <= y:
                            answer = max(answer,(1+x-sx)*(1+z-sy)*(1+y-sz))
                        if sx <= y and sy <= x and sz <= z:
                            answer = max(answer,(1+y-sx)*(1+x-sy)*(1+z-sz))
                        if sx <= y and sy <= z and sz <= x:
                            answer = max(answer,(1+y-sx)*(1+z-sy)*(1+x-sz))
                        if sx <= z and sy <= x and sz <= y:
                            answer = max(answer,(1+z-sx)*(1+x-sy)*(1+y-sz))
                        if sx <= z and sy <= y and sz <= x:
                            answer = max(answer,(1+z-sx)*(1+y-sy)*(1+x-sz))
                        '''
                    if sz <= y and sy <= z:
                        answer = max(answer,(1+x-sx)*(1+y-sz)*(1+z-sy))
    print(answer)
