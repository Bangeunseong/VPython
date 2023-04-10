from vpython import *

ball = sphere(radius = 0.2)
ground = box(pos = vec(0,0,0), size = vec(15,-0.01,5)) 

radian = radians(30)
ball.pos = vec(-2,0,0)
ball.v = vec(cos(radian),sin(radian), 0)*2
ball.a = vec(0,-0.35,0)

t = 0 
dt = 0.01

attach_arrow(ball, "v", shaftwidth = 0.1, color = color.green) 
attach_arrow(ball, "a", shaftwidth = 0.05, color = color.red)

attach_trail(ball, type = 'points', pps = 5)


motion_graph = graph(title = 'position-time', xtitle = 't', ytitle = 'y')
g_bally = gcurve()
motion_graph2 = graph(title = 'velocity-time', xtitle = 't', ytitle = 'vy') 
g_ballvy = gcurve(color = color.green)

while ball.pos.y >= ground.pos.y:
    rate(1/dt)

    ball.v = ball.v + ball.a*dt 
    ball.pos = ball.pos + ball.v*dt 

    g_bally.plot(pos = (t,ball.pos.y)) 
    g_ballvy.plot(pos = (t,ball.v.y)) 

    t += dt
print(ball.pos)