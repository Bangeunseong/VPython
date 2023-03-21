from vpython import *

#Number 1
a = vector(1,2,3)
b = vector(0,2,4)

print("**Number 1**")
print("inner product: ", a.dot(b), "\n")

#Number 2
r = vector(2,-2,2)

print("**Number 2**")
print("magnitude: ", mag(r))
print("norm: ", hat(r), "\n")

#Number 3
v = vector(3,4,0)
unit = vector(1,0,0)

parallel = v.dot(unit)*unit
perpendicular = v - parallel

print("**Number 3**")
print("parallel: ", parallel)
print("perpendicular: ", perpendicular)

origin = arrow(pos = vec(0,0,0), axis = v, shaftwidth = 0.2, color = color.white)
pr = arrow(pos = vec(0,0,0), axis = parallel, shaftwidth = 0.1, color = color.blue)
pp = arrow(pos = vec(0,0,0), axis = perpendicular, shaftwidth = 0.1, color = color.red)