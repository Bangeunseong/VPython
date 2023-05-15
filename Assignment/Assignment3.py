from vpython import *

ceiling = box(pos = vec(0,0,0), size = vec(0.4,0.01,0.4))
plate = box(pos = vec(0,-0.25,0), size = vec(0.4,0.05,0.05), v = vec(0,0,0), m = 1, kv = 0, color = color.orange, make_trail = True)
spring1 = helix(pos = ceiling.pos - vec(0.1,0,0), axis = plate.pos - ceiling.pos, color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)
spring2 = helix(pos = ceiling.pos - vec(0.035,0,0), axis = plate.pos - ceiling.pos, color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)
spring3 = helix(pos = ceiling.pos + vec(0.035,0,0), axis = plate.pos - ceiling.pos, color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)
spring4 = helix(pos = ceiling.pos + vec(0.1,0,0), axis = plate.pos - ceiling.pos, color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)

g = vec(0,-9.8,0)
r0 = 0.25
ks = 100

t = 0
dt = 0.01

scene.autoscale = True
scene.center = vec(0,-r0,0)

traj = gcurve(color = color.red)

while t < 5:
    rate(1/dt)

    r = mag(plate.pos)
    s = r - r0
    rhat = norm(plate.pos)

    Fgrav = plate.m*g
    Fspr = -ks*s*rhat
    Fdamp = -plate.kv*dot(plate.v,rhat)*rhat

    Fnet = Fgrav + 4*Fspr + Fdamp

    plate.v += Fnet/plate.m*dt
    plate.pos += plate.v*dt

    t += dt

    spring1.axis = plate.pos
    spring2.axis = plate.pos
    spring3.axis = plate.pos
    spring4.axis = plate.pos

    traj.plot(pos = (t,plate.pos.y))