t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    nums = set()
    s = 0
    answer = 0
    for i,ai in enumerate(a):
        s += ai
        nums.add(ai)
        if s % 2 == 0 and (s//2) in nums:
            answer += 1
    print(answer)
