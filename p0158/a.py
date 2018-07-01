n, k = map(int,input().split())
assert 1 <= k <= n <= 50

scores = list(map(int,input().split())) # given sorted decreasing
assert len(scores) == n

# ignore non positive scores
while len(scores) != 0 and scores[-1] <= 0: scores.pop()

k = min(k,len(scores))
if k == len(scores): print(k)
else:
    while k < len(scores) and scores[k-1] == scores[k]: k += 1
    print(k)
