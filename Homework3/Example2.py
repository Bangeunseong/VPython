from vpython import *

#Number 1
u = vec(1,2,3)
v = vec(7,-2,0)

v.z = -(u.x*v.x + u.y*v.y)/u.z
print("**Number 1**")
print("inner product: ", u.dot(v), "\n")

#Number 2
a = vector(1,2,3)
b = vector(2,-1,1)
c = a.cross(b)
d = b.cross(a)

print("**Number 2**")
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)

a_arrow = arrow(pos = vec(0,0,0), axis = a, shaftwidth = 0.2, color = color.white)
b_arrow = arrow(pos = vec(0,0,0), axis = b, shaftwidth = 0.2, color = color.white)
c_arrow = arrow(pos = vec(0,0,0), axis = c, shaftwidth = 0.5, color = color.green)
d_arrow = arrow(pos = vec(0,0,0), axis = d, shaftwidth = 0.5, color = color.magenta) 