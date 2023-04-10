from vpython import *

ball = sphere(radius = 0.2)
ball.v = vec(0,0,0)
ball.a = vec(0,-0.35,0)
ground = box(pos = vec(0,0,0), size = vec(15,-0.01,5)) 

degree = [30,35,40,45,50,55,60]
distance = []

t = 0 
dt = 0.01

attach_arrow(ball, "v", shaftwidth = 0.1, color = color.green) 
attach_arrow(ball, "a", shaftwidth = 0.05, color = color.red)

attach_trail(ball, type = 'points', pps = 5)

for deg in degree:
    ball.pos = vec(-2,0,0)
    ball.v = vec(cos(radians(deg)),sin(radians(deg)), 0)*2
    while ball.pos.y >= ground.pos.y:
        rate(1/dt)

        ball.v = ball.v + ball.a*dt 
        ball.pos = ball.pos + ball.v*dt 

        t += dt
    distance.append(ball.pos.x + 2)
print("degree |", degree)
print("distance |", distance)
