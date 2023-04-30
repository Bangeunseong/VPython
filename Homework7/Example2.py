from vpython import *

#2
#종단 속력 = 1/2*Fg/(Cd*P*A)
#P = 1, A = pi*radius, Fg = mg

scalefactor = 10

raindrop = sphere(pos = vec(0,250,0), radius = 0.5*scalefactor, mass = 5*10**-7, v = vec(0,0,0), color = color.white)
ground = box(pos = vec(0,-0.5,0), size = vec(8,1,8)*scalefactor, color = color.white)

g = vec(0, -9.8, 0)
Fg = raindrop.mass*g
k = raindrop.mass*mag(g)/20

t = 0
dt = 0.01

motion_graph = graph(title = "Velocity-Time", xtitle = "t", ytitle = "v")
raindrop_v = gcurve()

while mag(raindrop.pos - ground.pos) > raindrop.radius - ground.pos.y:
    rate(1/dt)
    raindrop_v.plot(pos = (t, -raindrop.v.y))
    airdrag = -k*raindrop.v
    raindrop.v += (Fg + airdrag)/raindrop.mass*dt
    raindrop.pos += raindrop.v*dt
    t += dt
