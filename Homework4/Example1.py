from vpython import *
import math

#**Number1**
#r(t) = (cos(pi*t),sin(pi*t),0)
#v(t) = (-pi*sin(pi*t), pi*cos(pi*t),0)
#a(t) = (-pi**2*cos(pi*t), -pi**2*sin(pi*t),0)

#**Number2**
#Calculated by handwriting
#r(0.5) = (0,1,0)
#v(0.5) = (-pi,0,0)
#a(0.5) = (0,-pi**2,0)

#**Number3**
#Calculated by Coding
t = 0.5
dt = 0.001

vec_v = (vec(cos(math.pi*(t + dt)), sin(math.pi*(t + dt)), 0) - vec(cos(math.pi*t), sin(math.pi*t), 0))/dt
print("v(t) :", vec_v)