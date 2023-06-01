from vpython import *

ball = sphere(pos = vec(0,10,0), radius = 0.1, v = vec(2,-2,0), a = vec(0,0,0), mass = 1, color = color.white, make_trail = True)

w = 0
t = 0
dt = 0.01
g = 9.8

while ball.pos.y > 0:
    rate(1/dt)
    r0 = ball.pos.y

    ball.v += ball.a*dt
    ball.pos += ball.v*dt

    w += ball.mass*g*abs(r0 - ball.pos.y)

    t += dt
print(ball.pos)
print(w, "N.m")