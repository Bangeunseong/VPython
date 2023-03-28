from vpython import *

#Same velocity movement
ball = sphere(radius = 0.2)
ball.pos = vec(-2,0,0)
ball.v = vec(0.8,0,0)

t = 0
dt = 0.01
attach_arrow(ball, "v", shaftwidth = 0.1, color = color.green)

while t<4:
    rate(1/dt)
    ball.pos += ball.v*dt
    t += dt


#Same acceleration movement
ball = sphere(radius = 0.2)
ball.pos = vec(-2,0,0)
ball.v = vec(0,0,0)
ball.a = vec(0.35,0,0)

t = 0
dt = 0.01

attach_arrow(ball,"v", shaftwidth = 0.1, color=color.green)
attach_arrow(ball,"a", shaftwidth = 0.05, color=color.red)
attach_trail(ball, type = 'points', pps = 5)

while t<4:
    rate(1/dt)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    t += dt


#Curve movement
ball = sphere(radius = 0.2)
ground = box(pos = vec(0,-4,0), size = vec(15,-0.01,5))

ball.pos = vec(-2,0,0)
ball.v = vec(1,1,0)
ball.a = vec(0,-0.35,0)

t = 0
dt = 0.01

attach_arrow(ball, "v", shaftwidth = 0.1, color=color.green)
attach_arrow(ball, "a", shaftwidth = 0.05, color=color.red)
attach_trail(ball, type = 'points', pps = 5)
#extra component Graph
motion_graph = graph(title = 'position-time', xtitle = 't', ytitle = 'y')
gbally = gcurve(graph = motion_graph)
motion_graph2 = graph(title = "velocity-time", xtitle = "t", ytitle = "vy")
gballvy = gcurve(color = color.green, graph = motion_graph2)

while ball.pos.y > ground.pos.y:
    rate(1/dt)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt

    gbally.plot(pos = (t,ball.pos.y))
    gballvy.plot(pos = (t,ball.v.y))
    t += dt