from vpython import *

#**Number1, Number2**
t = 0
dt = 0.001

box_A = box(pos = vec(-8,0,0), size = vec(2,1,1), color = color.red)
box_B = box(pos = vec(-8,2,0), size = vec(2,1,1), color = color.blue)

box_A.v = vec(3,0,0)
box_B.v = vec(0,0,0)
box_B.a = vec(1,0,0)

motion_graph = graph(title = 'position-time', xtitle = 't', ytitle = 'x')
g_boxA_x = gcurve(graph = motion_graph, color = color.red)
g_boxB_x = gcurve(graph = motion_graph, color = color.blue)

while box_A.pos.x >= box_B.pos.x:
    rate(1/dt)
    box_A.pos += box_A.v*dt
    box_B.v += box_B.a*dt
    box_B.pos += box_B.v*dt

    g_boxA_x.plot(pos = (t,box_A.pos.x))
    g_boxB_x.plot(pos = (t,box_B.pos.x))
    t += dt
print("Time =", t)
print("x =", box_B.pos.x)