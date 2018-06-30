import sys

n = int(input()) # num test cases
assert 1 <= n <= 10**5

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

# column number to its letter representation
# each letter is selected based on how many complete cycles the letters to the
# right of it went through
def to_base_26(num):
    global letters
    result = letters[(num-1)%26]
    num = (num-1)//26
    while num != 0:
        result += letters[(num-1)%26]
        num = (num-1)//26
    return result[::-1]

def to_integer(b26): # use value of each letter and sum them together
    result = 0
    base = 1
    for c in b26[::-1]:
        result += base * (ord(c) - ord('A') + 1)
        base *= 26
    return result

for line in sys.stdin:
    ci = line.find('C')
    if line[0] == 'R' and ci != -1: # test for R(num)C(num) form
        r = line[1:ci]
        if r.isdigit(): # valid row
            r = int(r)
            c = int(line[ci+1:])
            print(to_base_26(c),r,sep='')
            continue
    # form is (col letters)(row num)
    c = ''
    r = ''
    for char in line:
        if char in letters: c += char
        else: r += char
    r = int(r)
    c = to_integer(c)
    print('R',r,'C',c,sep='')
