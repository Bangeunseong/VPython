#2
#종단 속력 = 1/2*Fg/(Cd*P*A)
#P = 1, A = pi*radius, Fg = mg
from vpython import *

scalefactor = 10

raindrop = sphere(pos = vec(0,250,0), radius = 0.5*scalefactor, mass = 5*10**-7, v = vec(0,0,0), color = color.white)
ground = box(pos = vec(0,-1,0), size = vec(10,1,10)*scalefactor, color = color.white)

g = vec(0, -9.8, 0)
Fg = raindrop.mass*g
k = raindrop.mass*mag(g)/20

t = 0
dt = 0.01

motion_graph = graph(title = "Velocity-Time", xtitle = "t", ytitle = "v")
raindrop_v = gcurve(graph = motion_graph)

while mag(raindrop.pos) > raindrop.radius:
    rate(1/dt)
    raindrop_v.plot(pos = (t, -raindrop.v.y))
    airdrag = -k*raindrop.v
    raindrop.v += (Fg + airdrag)/raindrop.mass*dt
    raindrop.pos += raindrop.v*dt
    t += dt
