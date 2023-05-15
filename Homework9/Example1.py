from vpython import *

ceiling = box(pos = vec(0,0,0), size = vec(0.2,0.01,0.2))
ball1 = sphere(pos = vec(-0.05,-0.25,0), radius = 0.025, v = vec(0,0,0), m = 1, kv = 0.5, color = color.red, make_trail = True)
ball2 = sphere(pos = vec(0,-0.25,0), radius = 0.025, v = vec(0,0,0), m = 1, kv = 1, color = color.green, make_trail = True)
ball3 = sphere(pos = vec(0.05,-0.25,0), radius = 0.025, v = vec(0,0,0), m = 1, kv = 2, color = color.blue, make_trail = True)
spring1 = helix(pos = ceiling.pos - vec(0.05,0,0), axis = ball1.pos - ceiling.pos + vec(0.05,0,0), color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)
spring2 = helix(pos = ceiling.pos, axis = ball2.pos - ceiling.pos, color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)
spring3 = helix(pos = ceiling.pos + vec(0.05,0,0), axis = ball3.pos - ceiling.pos - vec(0.05,0,0), color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)

g = vec(0,-9.8,0)
r0 = 0.25
ks = 100

t = 0
dt = 0.01

scene.autoscale = True
scene.center = vec(0,-r0,0)

traj1 = gcurve(color = color.red)
traj2 = gcurve(color = color.green)
traj3 = gcurve(color = color.blue)

while t < 10:
    rate(1/dt)

    Fgrav = ball1.m*g
    r1 = mag(ball1.pos + vec(0.05,0,0))
    r2 = mag(ball2.pos)
    r3 = mag(ball3.pos - vec(0.05,0,0))

    s1 = r1 - r0
    s2 = r2 - r0
    s3 = r3 - r0

    rhat1 = norm(ball1.pos + vec(0.05,0,0))
    rhat2 = norm(ball2.pos)
    rhat3 = norm(ball3.pos - vec(0.05,0,0))

    Fspr1 = -ks*s1*rhat1
    Fspr2 = -ks*s2*rhat2
    Fspr3 = -ks*s3*rhat3

    Fdamp1 = -ball1.kv*dot(ball1.v,rhat1)*rhat1
    Fdamp2 = -ball2.kv*dot(ball2.v,rhat2)*rhat2
    Fdamp3 = -ball3.kv*dot(ball3.v,rhat3)*rhat3

    Fnet1 = Fgrav + Fspr1 + Fdamp1
    Fnet2 = Fgrav + Fspr2 + Fdamp2
    Fnet3 = Fgrav + Fspr3 + Fdamp3

    ball1.v += Fnet1/ball1.m*dt
    ball2.v += Fnet2/ball2.m*dt
    ball3.v += Fnet3/ball3.m*dt

    ball1.pos += ball1.v*dt
    ball2.pos += ball2.v*dt
    ball3.pos += ball3.v*dt

    t += dt

    spring1.axis = ball1.pos + vec(0.05,0,0)
    spring2.axis = ball2.pos
    spring3.axis = ball3.pos - vec(0.05,0,0)

    traj1.plot(pos = (t,ball1.pos.y))
    traj2.plot(pos = (t,ball2.pos.y))
    traj3.plot(pos = (t,ball3.pos.y))
