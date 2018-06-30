import math

a = tuple(map(float,input().split(' ')))
b = tuple(map(float,input().split(' ')))
c = tuple(map(float,input().split(' ')))

def vec(p1,p2): return (p2[0]-p1[0], p2[1]-p1[1]) # vector between 2 points
def dot(v1,v2): return v1[0]*v2[0] + v1[1]*v2[1] # vector dot product
def mag(v): return math.sqrt(v[0]**2 + v[1]**2) # vector magnitude

# first find the center of the circle
# if a,b,c are on a circle then angle between ab,ac is half the angle between
# ob,oc (o is center)
angle = 2.0*math.acos(dot(vec(a,b),vec(a,c)) / mag(vec(a,b)) / mag(vec(a,c)))

