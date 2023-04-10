from vpython import *

#Field
s = sphere(pos = vec(0,0,0), radius = 1, color = color.red)
arrow(axis = vec(4,0,0), color = color.white, shaftwidth = 0.1)
arrow(axis = vec(0,4,0), color = color.white, shaftwidth = 0.1)
#Time Field
t = 0
dt = 0.001

#distance, velocity, acceleration vectors
s.v = vec(2,0,0)
s.a = s.v.cross(vec(0,0,-1))
r = 0

#position graph of sphere s
motion_graph = graph(title = 'position-time', xtitle = 't', ytitle = 'y')
g_bally = gcurve()


while t < 8:
    rate(1/dt)
    s.pos += s.v*dt
    s.v += s.a*dt
    s.a = s.v.cross(vec(0,0,-1))
    g_bally.plot(pos = (t,s.pos.y))
    if r < s.pos.y:
        r = s.pos.y
    t += dt

print(r/2)