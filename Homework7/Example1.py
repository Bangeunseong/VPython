#1
#Mass가 1인 물체에 작용하는 힘은 mg 이때 물체는 비탈면을 미끄러져 내려오기에 비탈면에
#수직으로 작용하는 힘과 수평으로 작용하는 힘의 합력이 mg
#수평작용힘: mgsin(theta) 수직작용힘: mgcos(theta)
#비탈면의 길이는 10일때 10 = vi*t + 1/2*a*t**2
#a = gsin(theta) = 9.8*3/5 = 5.88
#vi = 0, 10*2/a = t**2, sqrt(10*2/a) = t
#t = 1.844...

#2
from vpython import *

serface = triangle(v0 = vertex(pos = vec(0,0,0), color = color.green), v1 = vertex(pos = vec(8,0,0), color = color.green), v2 = vertex(pos = vec(0,6,0), color = color.green))
ball = sphere(pos = vec(0,6,0), mass = 1, radius = 0.1, v = vec(0,0,0), color = color.white)

t = 0
dt = 0.01

a = vec(5.88*4/5, -5.88*3/5,0)

while ball.pos.y > 0:
    rate(1/dt)
    ball.v += a*dt
    ball.pos += ball.v*dt
    t += dt
print("Time :", t)
