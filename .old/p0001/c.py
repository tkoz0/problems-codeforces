import math

a = tuple(map(float,input().split(' ')))
b = tuple(map(float,input().split(' ')))
c = tuple(map(float,input().split(' ')))

assert all(abs(x) <= 1000.0 for x in a+b+c)

def vec(p1,p2): return (p2[0]-p1[0], p2[1]-p1[1]) # vector between 2 points
def dot(v1,v2): return v1[0]*v2[0] + v1[1]*v2[1] # vector dot product
def mag(v): return math.sqrt(v[0]**2 + v[1]**2) # vector magnitude

# angle between 2 vectors: cos(angle) = (v1 dot v2) / (|v1| * |v2|)
def angle(v1,v2): return math.acos(dot(v1,v2)/(mag(v1)*mag(v2)))

# is close enough to an integer
# started with 2**-32, was too small
def is_int(a):
    return abs(a-round(a)) < 2**-16

# compute arcs AB, AC, BC using the 3 points on the circle
arc_ab = 2*angle(vec(c,a),vec(c,b))
arc_ac = 2*angle(vec(b,a),vec(b,c))
arc_bc = 2*angle(vec(a,b),vec(a,c))

# determine number of sides, given that it will never be > 100
for sides in range(3,100+1):
    arc_side = 2*math.pi/sides
    sides_ab = arc_ab/arc_side
    sides_ac = arc_ac/arc_side
    sides_bc = arc_bc/arc_side
    if is_int(sides_ab) and is_int(sides_ac) and is_int(sides_bc):
        num_sides = sides
        break

if 'num_sides' not in dir():
    num_sides = -1 # should be wrong answer

# radius of circumcircle r = abc / (4*A) (side lengths and area)
len_ab = mag(vec(a,b))
len_ac = mag(vec(a,c))
len_bc = mag(vec(b,c))
s = (len_ab+len_ac+len_bc)/2
area = math.sqrt(s*(s-len_ab)*(s-len_ac)*(s-len_bc))
radius = len_ab*len_ac*len_bc / (4*area)

# compute area of regular polygon = n * r^2 * cos(a) * sin(a)
# a = 2*pi/(2n) = pi/n (n sides)
alpha = math.pi/num_sides
area_solution = num_sides * radius**2 * math.cos(alpha) * math.sin(alpha)

print(area_solution)
